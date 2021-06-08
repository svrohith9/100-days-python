from flask import Flask, redirect, request
from flask.templating import render_template
from wtforms.validators import DataRequired, URL
from wtforms.fields.core import RadioField, SelectField, StringField
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField
import flask
import csv
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
all_books = []
app.config['SECRET_KEY'] = 'any-secret-string'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BookForm(FlaskForm):
    name = StringField(label="Book Name", validators=[DataRequired()])
    author = StringField(label="Book Author", validators=[DataRequired()])
    rating = SelectField(label="Rating", validators=[
        DataRequired()], choices=[1, 2, 3, 4, 5])
    submit = SubmitField("submit")


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            data = Book(
                title=form.name.data,
                author=form.author.data,
                rating=int(form.rating.data)
            )
        # all_books.append(data)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
