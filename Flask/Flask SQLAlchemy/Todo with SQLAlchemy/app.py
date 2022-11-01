from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String, nullable=False)

db.create_all()


@app.route("/")
def index():
    task = request.args.get("task")
    if task:
        db.session.add(Todo(task=task))
        db.session.commit()
    tasks = Todo.query  # return a list
    return render_template("index.html", tasks=tasks)
