from flask.app import Flask
from flask.templating import render_template
from wtforms.validators import DataRequired, URL
from wtforms.fields.core import StringField

app = Flask(__name__)


class Data:
    name = StringField('Name', validators=[DataRequired()])
    url = StringField('Geo-Link', validators=[DataRequired(), URL()])
    food = StringField('Food 🍕', validators=[DataRequired()])
    spot = StringField('Spot 🏖️', validators=[DataRequired()])
    price = StringField('Price 💰', validators=[DataRequired()])


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
