import smtplib

my_email = ~~~~email~~~~
pwd = ~~~Password~~~~

to_mail = ~~~To_Mail~~~

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=pwd)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_mail",
        msg="Subject: Yo\n\n Harry potter is slytherin"
    )
