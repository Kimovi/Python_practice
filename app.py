#!/usr/bin/python3
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/Book"
app.config['SQLALchemy_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    book_title = db.Column(db.String(30), primary_key=True)
    author = db.Column(db.String(30))
    rating = db.Column(db.String(30))
    date_finished = db.Column(db.String(30))

# class User(db.Model):
#     u_name = db.Column(db.String(30), primary_key=True)
    #user_email = db.Column(db.String(30))

db.create_all()

@app.route('/', methods=["GET","POST"])
def home():
    if request.form:
        book_db = Book(book_title=request.form.get("book_title"))
        author_db = Book(author=request.form.get("author"))
        rating_db = Book(rating=request.form.get("rating"))
        date_finished_db = Book(date_finished=request.form.get("date"))
        # u_name = User(u_name=request.form.get("u_name"))
        db.session.add(book_db) 
        # db.session.add(u_name)
       	db.session.commit()
    book_lists = Book.query.all()
    # u_name = User.query.all()
    return render_template("home.html", book_lists=book_lists)

@app.route("/update", methods=["POST"])
def update():
    book_db = Book.query.filter_by(book_title=request.form.get("oldbook_title")).first()
    book_db.book_title = request.form.get("newbook_title")
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    book_db = Book.query.filter_by(book_title=request.form.get("book_title")).first()
    db.session.delete(book_db)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')