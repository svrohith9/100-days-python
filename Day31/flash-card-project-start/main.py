BACKGROUND_COLOR = "#B1DDC6"

import random
import tkinter
import time
import pandas as pd

language_data = pd.read_csv(
    "https://raw.githubusercontent.com/svrohith9/100-days-python/acdbadfb1baa070c178a8fed258746403406ad5a/Day31/flash-card-project-start/data/french_words.csv"
)
language_dic = language_data.to_dict(orient="records")
current_card = {}


def run_random():
    global current_card, flip_timer
    try:
        current_card = random.choice(language_dic)
    except IndexError:
        canvas.itemconfig(card_title, text="You are all Caught Up !", fill="white")
        canvas.itemconfig(card_word, text="", fill="white")

    window.after_cancel(flip_timer)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=card_flip)


def card_flip():
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


def correct_run_random():
    try:
        language_dic.remove(current_card)
    except ValueError:
        canvas.itemconfig(card_title, text="You are all Caught Up !", fill="white")
        canvas.itemconfig(card_word, text="", fill="white")
    else:
        run_random()


window = tkinter.Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=card_flip)

canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage(
    file=".\\100-days-python\\Day31\\flash-card-project-start\\images\\card_front.png"
)
card_back_img = tkinter.PhotoImage(
    file=".\\100-days-python\\Day31\\flash-card-project-start\\images\\card_back.png"
)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))

cross_image = tkinter.PhotoImage(
    file=".\\100-days-python\\Day31\\flash-card-project-start\\images\\wrong.png"
)
cross_button = tkinter.Button(
    image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=run_random
)
cross_button.grid(row=1, column=0)


right_image = tkinter.PhotoImage(
    file=".\\100-days-python\\Day31\\flash-card-project-start\\images\\right.png"
)
right_button = tkinter.Button(
    image=right_image,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=correct_run_random,
)
right_button.grid(row=1, column=1)


canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


run_random()
window.mainloop()
