#!/usr/bin/python3
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALchemy_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    book_title = db.Column(db.String(30), nullable=False, primary_key=True)

class User(db.Model):
    user_name = db.Column(db.String, primary_key=True)
    user_email = db.Column(db.String)

db.create_all()

@app.route('/', methods=["GET","POST"])
def home():
    if request.form:
        book_db = Book(book_title=request.form.get("book_title"))
        db.session.add(book_db)
        db.session.commit()
    registrees = Book.query.all()
    return render_template("home.html", registrees=registrees)

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


# from flask import Flask, redirect, render_template, request, url_for
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/Register"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Register(db.Model):
#     name = db.Column(db.String(30), nullable=False, primary_key=True)

# # class Book(db.Model):
# #     book_title = db.Column(db.String(30), primary_key=True, nullable = False, autoincrement=True)
#     # book_id = db.Column(db.Integer, db.ForeignKey("register.name"), nullable=False)
#     # date_finished = db.Column(db.DateTime)
#     # rating = db.Column(db.Integer)
#     # review = db.Column(db.String(30))

# db.create_all()

# @app.route('/', methods=["GET","POST"])
# def home():
#     if request.form:
#         person = Register(name=request.form.get("name"))
#         # book = Book(book_title=request.form.get("book_title"))
#         db.session.add(person)
#         db.session.commit()
#     registrees = Register.query.all() 
#     # book_lists = Book.query.all()
#     return render_template("home.html", registrees = registrees)

# @app.route("/update", methods=["POST"])
# def update():
#     person = Register.query.filter_by(name=request.form.get("oldname")).first()
#     person.name = request.form.get("newname")
#     db.session.commit()
#     return redirect("/")

# @app.route("/delete", methods=["POST"])
# def delete():
#     person = Register.query.filter_by(name=request.form.get("name")).first()
#     db.session.delete(person)
#     db.session.commit()
#     return redirect("/")

# if __name__ == '__main__':
#     app.run(port=5000, debug=True, host='0.0.0.0')
