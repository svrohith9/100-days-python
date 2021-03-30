import tkinter
import random
from tkinter.constants import E, END
from typing import Text


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=30, pady=50)


# Canvas logo
canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file=".\\Day29\\password-manager\\logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0, columnspan=2)


# Add Data Button
def submit_data():
    w = website.get()
    e = email.get()
    p = password.get()
    with open(file=".\\Day29\\password-manager\\pwd-list.txt", mode="a") as data:
        data.write(f"{w}, {e}, {p}\n")

    website.delete(0, END)
    password.delete(0, END)


# Generate password button


# Website box with label
website = tkinter.Entry(width=40)
website.grid(column=1, row=1, columnspan=2)
website.focus()  # default cursor location

website_label = tkinter.Label(text="Website :")
website_label.grid(column=0, row=1)

# email box with label
email = tkinter.Entry(width=40)
email.grid(column=1, row=2, columnspan=2)
email.insert(0, "harrypotter@hogwards.com")  # frequent used mail

email_label = tkinter.Label(text="UserName :")
email_label.grid(column=0, row=2)


# password box with label
password = tkinter.Entry(width=20)
password.grid(column=1, row=3)

password_label = tkinter.Label(text="Password :")
password_label.grid(column=0, row=3)

# Generate password button
gen_pwd_btn = tkinter.Button(text=" Generate password", bg="white", width=20)
gen_pwd_btn.grid(column=2, row=3)

# Submit Button
submit = tkinter.Button(text="Add Data", width=50, command=submit_data)
submit.grid(column=1, row=4, columnspan=2)

window.mainloop()
