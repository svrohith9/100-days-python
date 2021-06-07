from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, InputRequired


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


app = Flask(__name__)
app.secret_key = "random-secret"


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
        if login_form.email.data == 'admin@admin.com' and login_form.password.data == 'admin@123':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=login_form)


@app.route("/success")
def success():
    return "<h1>login Sucessful</h1>"


@app.route("/denied")
def denied():
    return "<h1>login Failed</h1>"


if __name__ == '__main__':
    app.run(debug=True)
