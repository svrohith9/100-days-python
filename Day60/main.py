from flask.app import Flask, request
from flask.templating import render_template
import smtplib

app = Flask(__name__)
BASE_URL = "http://localhost:5000"
EMAIL = "your email id"
PASSWORD = "your password"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form["username"]
    password = request.form["password"]
    return render_template('contact.html')


def mail_to_usr(name, email, sub, message):
    email_message = f"Subject:{sub}\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)


@app.route('/sendMail', methods=['POST'])
def send_mail():
    name = request.form['name']
    email = request.form['email']
    sub = request.form['sub']
    message = request.form['message']
    try:
        mail_to_usr(name, email, sub, message)
        return f"<h1>Sucessfully received your message</h1>"
    except:
        return f"<h1>Issue sending your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
