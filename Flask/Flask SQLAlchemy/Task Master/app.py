from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(30), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Task %r>' %self.id

db.create_all()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get("content")
        db.session.add(Todo(content=content))
        db.session.commit()
        return redirect("/")

    tasks = Todo.query
    # also valid
    # tasks = db.session.query(Todo)
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
    # will get the id or 404 if not exist
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form["content"]
        db.session.commit()
        return redirect("/")

    return render_template("update.html", task=task)