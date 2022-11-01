import flask
# from flask_mail import Mail, Message
import flask_mail

app = flask.Flask(__name__)

# sender email information configuration
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp-mail.outlook.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'asadhusn007@outlook.com',
    MAIL_PASSWORD = 'Zarfisha'
))

mymail = flask_mail.Mail(app)


@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route('/register', methods=["POST"])
def register():
    name = flask.request.form.get("Name")
    email = flask.request.form.get("Email")
    sub = flask.request.form.get("Subject")
    message = flask.request.form.get("Message")

    # outgoing message
    msg = flask_mail.Message(subject=sub,
        sender= (name,"asadhusn007@outlook.com"),
        recipients=[email],
        body=message)
    mymail.send(msg)
    # message sent confirmation
    return "Your mail has been sent!"