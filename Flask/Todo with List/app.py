from flask import Flask, request, redirect, render_template

app = Flask(__name__)

ITEMS = []

@app.route("/")
def index():
    item = request.args.get("item")
    if item:
        ITEMS.append(item)
    return render_template("index.html", items=ITEMS)
