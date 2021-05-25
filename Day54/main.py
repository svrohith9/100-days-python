from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper


def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper


@app.route('/')
@make_underlined
def hello_world():
    return "Hello"


@app.route('/bye')
@make_underlined
def bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)
