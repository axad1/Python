import flask
import flask_session

app = flask.Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

flask_session.Session(app)

@app.route("/")
def index():
    if not flask.session.get("name"):
        return flask.render_template("login.html")
    return flask.render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        flask.session["name"] = flask.request.form.get("name")
    return flask.render_template("index.html")

@app.route("/logout")
def logout():
    flask.session["name"] = None
    return flask.redirect("/")