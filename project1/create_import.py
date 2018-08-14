import os, csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

# TO IMPORT CSV FILE
# def main():
#     file = open("books_dup.csv")
#     read = csv.reader(file)
#     for isbn_, title_, author_, year_ in read:
#         books = Books(isbn=isbn_, title=title_, author=author_, year=year_)
#         db.session.add(books)
#     db.session.commit()
#     file.close()
#     print("PROGRESS COMPLETE")


if __name__ == "__main__":
    with app.app_context():
        main()
