import flask
import flask_wtf, wtforms
import flask_sqlalchemy
import datetime
import flask_login

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = flask_sqlalchemy.SQLAlchemy(app)
# ctx = app.app_context()
# ctx.push()

login_mgr = flask_login.LoginManager(app)
@login_mgr.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    phone = db.Column(db.String, nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text)
    password = db.Column(db.String, nullable=False)

class RegisterForm(flask_wtf.FlaskForm):
    name = wtforms.StringField(label='Name:')
    email = wtforms.EmailField(label='Email')
    phone = wtforms.TelField(label='Phone')
    dob = wtforms.DateField(label='Date of Birth')
    text = wtforms.TextAreaField(label='Comment')
    password = wtforms.PasswordField(label='Password:')
    submit = wtforms.SubmitField(label='Register')

class LoginForm(flask_wtf.FlaskForm):
    email = wtforms.EmailField(label='Email')
    password = wtforms.PasswordField(label='Password:')
    submit = wtforms.SubmitField(label='Login')

# db.drop_all()
# db.create_all()

@app.route('/')
@app.route('/login', methods=['GET', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            flask_login.login_user(user)
            flask.flash('Success! ' + user.name + ' logged in')
        else:
            flask.flash('Password not correct')

        if form.errors:
            for err in form.errors.values():
                flask.flash(err)
        return flask.redirect(flask.url_for('login'))

    return flask.render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        dob = form.dob.data
        text = form.text.data
        password = form.password.data

        if form.errors:
            for err in form.errors.values():
                flask.flash(err)

        try:
            db.session.add(User(name=name, email=email, phone=phone, dob=dob, text=text, password=password))
            db.session.commit()
        except Exception as e:
            flask.flash(e)
        else:                
            flask.flash('User Registered')

    return flask.render_template('register.html', form=form)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    flask.flash('You are logged out')
    return flask.redirect(flask.url_for('login'))