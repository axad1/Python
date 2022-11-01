from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, InputRequired, ValidationError
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, UserMixin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    item = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(30), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=0)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, text):
        self.password_hash = bcrypt.generate_password_hash(text).decode('utf-8')

    def check_password(self, attempted):
        return bcrypt.check_password_hash(self.password_hash, attempted)


class RegisterForm(FlaskForm):

    def validate_username(self, user_check):
        user = User.query.filter_by(name=user_check.data).first()
        if user:
            raise ValidationError('Username already exist!')

    def validate_email(self, email_check):
        email = User.query.filter_by(email=email_check.data).first()
        if email:
            raise ValidationError('Email already exist!')

    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired(), InputRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Repeat Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')
    


# db.drop_all()
# db.create_all()

# items = [
#     {
#         'name': 'Phone',
#         'price': 200
#     },
#     {
#         'name': 'Laptop',
#         'price': '900'
#     },
#     {
#         'name': 'Keyboard',
#         'price': 300
#     }
# ]

# for item in items:
#     db.session.add(Item(name=item['name'], price=item['price']))
# db.session.commit()


@app.route('/')     # Decorator
def home():
    return render_template("index.html")

@app.route('/market')
def market():
    result = Item.query.all()
    return render_template("market.html", items=result)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.username.data,
                    email=form.email.data,
                    password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', category='success')
        return redirect(url_for('market'))
    if form.errors:
        for err in form.errors.values():
            flash(err, category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user and user.check_password(attempted=form.password.data):
            login_user(user)
            flash('Success! You are logged in', category='success')
            return redirect(url_for('market'))
        else:
            flash('Password not matched!', category='danger')
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out successfully", category='info')
    return redirect(url_for('home'))
