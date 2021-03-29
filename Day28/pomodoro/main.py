import tkinter
from typing import Text

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=150, pady=100)

# Timer label

label = tkinter.Label(text="TIMER", fg=GREEN, font=("Verdana", 40))
label.grid(column=1, row=0)


# Tomato and Timer text
canvas = tkinter.Canvas(width=400, height=300)
image = tkinter.PhotoImage(file=".\\Day28\\pomodoro\\tomato.png")
canvas.create_image(200, 150, image=image)
canvas.create_text(200, 170, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# start button


def start_timer():
    canvas.config(text="Hello")


start = tkinter.Button(text="start", command=start_timer, bg="white")
start.grid(column=0, row=2)

# ticks label to identify no of
ticks = tkinter.Label(text="✓", fg=PINK, font=("Verdana", 20, "bold"))
ticks.grid(column=1, row=3)


# reset button

reset = tkinter.Button(text="reset", command=start_timer, bg="white")
reset.grid(column=2, row=2)


window.mainloop()
