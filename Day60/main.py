from flask.app import Flask, request
from flask.templating import render_template

app = Flask(__name__)
BASE_URL = "http://localhost:5000"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}"


if __name__ == "__main__":
    app.run(debug=True)
