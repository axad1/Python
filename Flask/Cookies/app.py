import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route("/setcookie", methods=['POST', 'GET'])
def setcookie():
    if flask.request.method == 'POST':
        user = flask.request.form['nm']
        resp = flask.make_response(flask.render_template("readcookie.html"))
        resp.set_cookie("userID", user)
        return resp

@app.route("/getcookie")
def getcookie():
    name = flask.request.cookies.get('userID')
    return "Welcome " + name
