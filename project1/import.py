import os, csv

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
# if not os.getenv("DATABASE_URI"):
#     raise RuntimeError("DATABASE_URI is not set")

db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
DATABASE_URI = 'sqlite:///{}'.format(db_path)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URI"))

engine = create_engine(DATABASE_URI)
db = scoped_session(sessionmaker(bind=engine))

# Import db
def main():
    file = open("books.csv")
    read = csv.reader(file)
    first = False
    for isbn, title, author, year in read:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
        {"isbn":isbn, "title":title, "author":author, "year":year})
    db.commit()
    file.close()
    print("Database 'books' imported")



main()
