from flask.app import Flask
from flask.templating import render_template
import random
from datetime import date
import requests

app = Flask(__name__)
GENDER_URL = "https://api.genderize.io?name="
AGE_URL = "https://api.agify.io?name="


@app.route('/')
def hello():
    random_number = random.randint(0, 9)
    current_date = date.today().year
    return render_template('index.html', random_number=random_number, date=current_date)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url=f"{GENDER_URL}{name}")
    response.raise_for_status()
    gender = response.json()['gender']

    response = requests.get(url=f"{AGE_URL}{name}")
    response.raise_for_status()
    age = response.json()['age']
    return render_template('guess.html', age=age, gender=gender, name=name)


if __name__ == "__main__":
    app.run(debug=True)
