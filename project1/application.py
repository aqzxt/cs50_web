import os, requests
from flask import (Flask, session, render_template, request, flash, jsonify)
from flask_session import Session
from flask_scss import Scss

from models import *

if not os.getenv("DATABASE_URL"): raise RuntimeError("DATABASE_URL is not set")

GOODREADS_APIKEY = os.getenv("GOODREADS_APIKEY")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)

Scss(app, static_dir='static', asset_dir='./assets/style')

# Homepage/Login/Register page
@app.route("/", methods=["GET", "POST"])
def main():
    # Login form user input
    email_login = request.form.get("email_login")
    password_login = request.form.get("password_login")

    # Registration form user input
    name_register = request.form.get("name_register")
    email_register = request.form.get("email_register")
    password_register = request.form.get("password_register")

    if request.method == "POST":
        # FOR LOGIN
        # Search for user/password in db
        user = Users.query.filter_by(email=email_login, password=password_login).first()
        if user:
            # Create and/or store user session credentials
            if session.get("email") is None:
                session["id"] = user.id
                session["name"] = user.name
                session["email"] = user.email
                session["password"] = user.password

            return render_template('members.html', name=user.name, email=user.email)

        # FOR REGISTRATION
        if name_register and "@" in email_register and password_register:
            # Check if chosen email is already used
            user = Users.query.filter_by(email=email_register, password=password_register).first()
            if user:
                return render_template("notify.html", msg="Email already registered. Please pick another one.")

            # Otherwise, populate db
            register = Users(email=email_register, name=name_register, password=password_register)
            db.session.add(register)
            db.session.commit()

            # Take user to success page
            return render_template('notify.html', title="Success", msg="Registration successfully done.")

        # Otherwise render error page
        return render_template('notify.html', title="Invalid credentials.", msg="Did you registered yet?")

    # If method == "GET"
    return render_template("main.html")


@app.route("/members", methods=["GET", "POST"])
def members():
    # Check if user is logged in before accessing the member's page
    if session.get("id") is None:
        return render_template("notify.html", title="Missing user credentials", msg="Please, go to the homepage to login.")

    category = request.form.get("category")
    query = request.form.get("query")

    session["category"] = category
    session["query"] = query

    if request.method == "POST":
        if category and query:
            return render_template("search.html", category=category, query=query)

        return render_template("notify.html", title="Invalid selection", msg="Category not selected or invalid query text.")

    # If method == "GET"
    return render_template("members.html", email=session.get("email"), name=session.get("id"))


@app.route("/search", methods=["GET", "POST"])
def search():
    # Check if user is logged in before accessing the search page
    if session.get("id") is None:
        return render_template("notify.html", title="Missing user credentials", msg="Please, go to the homepage to login.")

    # if request.method == "POST":
    category = request.form.get("category")
    query = request.form.get("query")
    if category == "year" and len(query) != 4:
        try:
            query = int(query)
        except:
            return render_template("notify.html", title="Invalid year", msg="Please, go back and try again.")

    obj = Books.query.filter(getattr(Books, category).ilike("%" + query + "%"))
    results = []
    for item in obj: results.append(item)
    return render_template("search.html", category=category, query=query, results=results)


@app.route("/search/<int:book_id>", methods=["GET","POST"])
def book(book_id):
    query = session.get("query")
    # Check if user is logged in before accessing the book page
    if session.get("id") is None:
        return render_template("notify.html", title="Missing user credentials", msg="Please, go to the homepage to login.")

    book = Books.query.get(book_id)
    if book is None:
        return render_template("notify.html", title="Error", msg="Invalid book id")

    user_id = session.get("id")
    user_reviews = Reviews.query.filter_by(user_id=user_id).all()

    if request.method == "GET":
        numbers = [i for i in range(1, 6)]
        numbers.insert(0, '')
        req = requests.get("https://www.goodreads.com/book/review_counts.json",
                params={"key": GOODREADS_APIKEY, "isbns": {book.isbn}}).json()["books"][0]
        return render_template("book.html", book=book, user_reviews=user_reviews, reviews_count=req["reviews_count"], average_rating=req["average_rating"], numbers=numbers, query=query)

    # if method == "POST"
    opinion = request.form.get("opinion")
    rate = request.form.get("rate")

    if not rate or not opinion:
        return render_template("notify.html", title="Invalid input", msg="Review or rate cannot be empty")

    for item in user_reviews:
        if item.user_id == user_id and item.isbn == book.isbn:
            return render_template("notify.html", title="Reviewed already sent", msg="Only one review per book is allowed.")

    user_reviews = Reviews(opinion=opinion, rate=rate, isbn=book.isbn, user_id=user_id)
    db.session.add(user_reviews)
    db.session.commit()

    # return render_template("book.html", opinion=opinion, rate=rate, user_reviews=user_reviews, msg="Your review were successfully sent.")
    return render_template("notify.html", title="Submitted", msg="Your review were successfully sent")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    if session.get("id") is None:
        return render_template("notify.html", title="Missing user credentials", msg="Please, go to the homepage to login.")

    if request.method == "GET":
        # Clear out user data
        session["user_id"] = []
        session["user_query"] = []
        return render_template("main.html", msg="You were successfully logged out")

    return render_template("notify.html", title="Not logged", msg="You need to be logged before logging out.")


@app.route("/notify.html", methods=["GET", "POST"])
def notify():
    if session.get("id") is None:
        return render_template("notify.html", title="Missing user credentials", msg="Please, go to the homepage to login.")

    if request.method == "POST":
        return render_template("notify.html", title="Success", msg="You registered successfully.")
    return render_template("notify.html", title="Error", msg="If you didn't submit the registration form why are you here?")


@app.route("/api/<string:isbn>", methods=["GET", "POST"])
def api(isbn):
    if request.method == "GET":
        book = Books.query.filter_by(isbn=isbn).first()
        if book is None:
            return jsonify({"error": "Book ISBN not found"}), 404

        reviews_count = Reviews.query.filter_by(isbn=isbn).count()
        isbn_matches = Reviews.query.filter_by(isbn=isbn).all()

        average_rating = 0
        if reviews_count is None:
            reviews_count = 0
        else:
            if isbn_matches:
                average = []
                for i in isbn_matches: average.append(isbn_matches.rate)
                average_rating = sum(average) // len(isbn_matches)

        return jsonify({
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "isbn": book.isbn,
                "reviews_count": reviews_count,
                "average_rating": average_rating
            })
    return render_template("notify.html", title="Error", msg="Invalid HTTP method")
