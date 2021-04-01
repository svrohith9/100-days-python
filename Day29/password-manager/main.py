import tkinter
import random
from tkinter.constants import E, END
from typing import Text
from tkinter import messagebox
import json


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=30, pady=50)

# password Gen


def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    passkey = ""

    for i in range(1, nr_letters+1):
        passkey = passkey + random.choice(letters)
    for i in range(1, nr_symbols+1):
        passkey = passkey + random.choice(symbols)
    for i in range(1, nr_numbers+1):
        passkey = passkey + random.choice(numbers)
    password_list = list(passkey)
    random.shuffle(password_list)
    password.insert(0, "".join(password_list))


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

    data_dto = {
        w: {
            "email": e,
            "password": p
        }
    }

    if w == "" or e == "" or p == "":
        messagebox.showerror(
            title="Error", message="Mandatory fields missing !")
    else:
        if messagebox.askokcancel(title=w, message=f"Email: {e}\n Password: {p}"):
            try:
                with open(file=".\\Day29\\password-manager\\pwd-list.json", mode="r") as data:
                    current_json_data = json.load(data)
                    current_json_data.update(data_dto)
            except FileNotFoundError:
                current_json_data = data_dto
            finally:
                with open(file=".\\Day29\\password-manager\\pwd-list.json", mode="w") as data:
                    json.dump(current_json_data, data, indent=4)
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
gen_pwd_btn = tkinter.Button(
    text=" Generate password", bg="white", width=20, command=generate_pwd)
gen_pwd_btn.grid(column=2, row=3)

# Submit Button
submit = tkinter.Button(text="Add Data", width=50, command=submit_data)
submit.grid(column=1, row=4, columnspan=2)

window.mainloop()
