import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    # Create stocks table
    sql = '''CREATE TABLE IF NOT EXISTS stocks(
        userid INTEGER,
        name TEXT NOT NULL,
        symbol TEXT NOT NULL,
        price INTEGER NOT NULL,
        shares INTEGER NOT NULL,
        FOREIGN KEY(userid) REFERENCES users(id) ON DELETE CASCADE
        )'''
    db.execute(sql)

    # Show portfolio of stocks
    rows = db.execute("SELECT * FROM stocks JOIN users ON id=userid where userid=?", session["user_id"])
    return render_template("index.html", stocks=rows)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # Buy shares of stock
    if request.method == "POST":
        # Ensure symbol was submitted
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol", 403)

        # Ensure shares was submitted
        shares = request.form.get("shares")
        if not shares or int(shares)<1:
            return apology("invalid shares", 403)
        shares = int(shares)
        # Ensure validation of symbol
        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol", 403)

        # stock = {
        # "name": "NETFLIX",
        # "price": 5,
        # "shares": 10
        # }
        # Check available cash
        rows = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
        if rows[0]["cash"] < shares*stock["price"]:
            return apology("You don't have enough cash", 403)
        
        db.execute("INSERT INTO stocks VALUES(?,?,?,?,?)",session["user_id"],symbol,stock["name"],stock["price"],shares)
        db.execute("UPDATE users SET cash=? WHERE id=?", rows[0]["cash"]-(shares*stock["price"]), session["user_id"])
        return redirect("/")

    return render_template("buy.html")
    

@app.route("/history")
@login_required
def history():
    # Show history of transactions
    rows = db.execute("SELECT * FROM stocks WHERE userid=?", session["user_id"])
    return render_template("history.html", stocks=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        stock = lookup(request.form.get("symbol"))
        # stock = {
        # "symbol": "NFLX",
        # "name": "NETFLIX",
        # "price": 5
        # }
        if not stock:
            return apology("symbol doesn't exist", 403)
        return render_template("quoted.html", stock=stock)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure correct password repeat was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password repeat", 403)

        # Ensure correct password repeat was submitted
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password must matched", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) == 1:
            return apology("username already exist", 403)
        
        # Add user in the database
        db.execute("INSERT INTO users(username,hash) VALUES(?,?)", request.form.get("username"), generate_password_hash(request.form.get("password")))

        # Remember which user has logged in
        # session["user_id"] = 1;

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        # Ensure symbol was submitted
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol", 403)

        rows = db.execute("SELECT * FROM stocks JOIN users ON id=userid WHERE userid=? AND symbol=?", session["user_id"], symbol)

        # Ensure shares was submitted
        shares = request.form.get("shares")
        if not shares or int(shares)<1:
            return apology("invalid shares", 403)
        if int(shares)>rows[0]["shares"]:
            return apology("you don't have that much shares", 403)

        shares = int(shares)
        db.execute("UPDATE stocks SET shares=? WHERE userid=? AND symbol=?", rows[0]["shares"]-shares, session["user_id"], symbol)
        db.execute("UPDATE users SET cash=? WHERE id=?", rows[0]["cash"]+shares*rows[0]["price"], session["user_id"])
        return redirect('/')

    """Sell shares of stock"""
    rows = db.execute("SELECT symbol FROM stocks WHERE userid=?", session["user_id"])
    return render_template("sell.html", symbols=rows)
