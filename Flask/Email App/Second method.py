# from flask import Flask, render_template, request
import flask
from flask_mail import Mail, Message

app = flask.Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee", "Football"]

app.config["MAIL_DEFAULT_SENDER"] = "asadhusn007@outlook.com"
app.config["MAIL_SERVER"] = 'smtp-mail.outlook.com'
app.config["MAIL_USERNAME"] = 'AsAdHusn007@outlook.com'
app.config["MAIL_PASSWORD"] = 'Zarfisha'
app.config["Mail_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False


mail = Mail(app)


@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/register", methods=["post"])
def register():

    # validate name and sport
    name = flask.request.form.get("Name")
    sub = flask.request.form.get("Subject")
    email = flask.request.form.get("Email")

    if not name or not email or not sub:
        return "Something is missing"

    # send email
    msg = Message("You are registered!", recipients=[email])
    mail.send(msg)
    return "Your mail has been sent!"
