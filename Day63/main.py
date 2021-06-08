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

app = Flask(__name__)
all_books = []
app.config['SECRET_KEY'] = 'any-secret-string'
Bootstrap(app)

db = sqlite3.connect("books-collection.db")


class Book(FlaskForm):
    name = StringField(label="Book Name", validators=[DataRequired()])
    author = StringField(label="Book Author", validators=[DataRequired()])
    rating = SelectField(label="Rating", validators=[
        DataRequired()], choices=[1, 2, 3, 4, 5])
    submit = SubmitField("submit")


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    data = {}
    form = Book()
    if request.method == "POST":
        if form.validate_on_submit():
            data = {
                "title": form.name.data,
                "author": form.author.data,
                "rating": int(form.rating.data)
            }
        all_books.append(data)
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run()
