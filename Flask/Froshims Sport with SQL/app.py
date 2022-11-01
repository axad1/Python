# from flask import Flask, render_template, request
import flask
import cs50

app = flask.Flask(__name__)

db = cs50.SQL("sqlite:///froshims.db")

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee", "Football"]

@app.route("/")
def index():
    REGISTRANTS = db.execute("SELECT * FROM registrants")
    return flask.render_template("index.html", registrants=REGISTRANTS, sports=SPORTS)

@app.route("/register", methods=["post"])
def register():

    # validate name and sport
    name = flask.request.form.get("name")
    sport = flask.request.form.get("sport")

    if not name or sport not in SPORTS:
        return flask.render_template("error.html")

    # save registration
    db.execute("INSERT INTO registrants(name,sport) VALUES(?,?)", name, sport)

    # confirm registration
    return flask.redirect("/")

@app.route("/deregister", methods=["post"])
def deregister():
    id = flask.request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id=?", id)
    return flask.redirect("/")
