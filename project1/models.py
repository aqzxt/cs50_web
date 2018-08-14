from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password


class Reviews(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    opinion = db.Column(db.String)
    rate = db.Column(db.Integer)
    isbn = db.Column(db.String)
    user_id = db.Column(db.Integer)

    def __init__(self, opinion=None, rate=None, isbn=None, user_id=None):
        self.opinion = opinion
        self.rate = rate
        self.isbn = isbn
        self.user_id = user_id
