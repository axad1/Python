import flask, wtforms, flask_wtf, flask_sqlalchemy

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = flask_sqlalchemy.SQLAlchemy(app)


class TodoForm(flask_wtf.FlaskForm):
    todo = wtforms.StringField(validators=[wtforms.validators.DataRequired()])


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String)

# with app.app_context():
#     db.drop_all()
#     db.create_all()

@app.route("/", methods=['GET', 'POST'])
@app.route('/<id>', methods=['GET', 'POST'])
def index(id=None):
    form = TodoForm()
    if id:
        todo = Todo.query.get(id)
        if todo:
            db.session.delete(Todo.query.get(id))
            db.session.commit()
        return flask.redirect(flask.url_for('index'))
        
    if form.validate_on_submit():
        db.session.add(Todo(todo=form.todo.data))
        db.session.commit()
        return flask.redirect(flask.url_for('index'))

    return flask.render_template("index.html", form=form, todos=db.session.query(Todo).order_by(db.desc(Todo.id)))