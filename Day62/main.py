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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-string'
Bootstrap(app)


class Data(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    url = StringField(
        'Geo-Link', validators=[DataRequired(), URL()])
    food_rating = SelectField('Food 🍕', choices=[
        '🍕', '🍕🍕', '🍕🍕🍕', '🍕🍕🍕🍕', '🍕🍕🍕🍕🍕'], validators=[DataRequired(message="Please Choose rating")])
    spot_rating = SelectField('Spot 🏖️', choices=[
        '🏖️', '🏖️🏖️', '🏖️🏖️🏖️', '🏖️🏖️🏖️🏖️', '🏖️🏖️🏖️🏖️🏖️'], validators=[DataRequired(message="Please Choose rating")])
    price_rating = RadioField('Price 💰', choices=[
        '💰', '💰💰', '💰💰💰', '💰💰💰💰', '💰💰💰💰💰'], validators=[DataRequired(message="Please Choose rating")], validate_choice=True)
    submit = SubmitField("submit")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/delete', methods=["POST", "GET"])
def delete():
    message = ""
    if request.method == "POST":
        pass
    return render_template('delete.html', message=message)


@app.route('/add', methods=["GET", "POST"])
def add():
    data = Data()
    message = ""
    if flask.request.method == 'POST':
        if data.validate_on_submit():
            with open(".\\100-days-python\\Day62\\data.csv", mode="a", encoding='utf8') as csv_file:
                csv_file.write(f"{data.name.data},"
                               f"{data.url.data},"
                               f"{data.food_rating.data},"
                               f"{data.spot_rating.data},"
                               f"{data.price_rating.data}\n")
                message = "Sucessfully added"
        else:
            message = "failed to add data"
    return render_template('add_data.html', form=data, message=message)


@app.route('/all')
def all():
    dataset = []
    with open('.\\100-days-python\\Day62\\data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for row in csv_data:
            dataset.append(row)
        print(dataset)
    return render_template('view_all.html', dataset=dataset)


if __name__ == "__main__":
    app.run(debug=True)
