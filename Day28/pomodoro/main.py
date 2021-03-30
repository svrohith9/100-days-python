import tkinter
from typing import Text
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
tick = ""
timer = None


def start_timer():
    global rep, tick
    rep += 1
    # pomodoro 20min <-> 5min X 4
    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN)
        label.config(text="Long Break", fg=RED)
        tick = ""
        ticks.config(text=tick)
    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN)
        label.config(text="Work Mode", fg=GREEN)
        tick += "✓"
        ticks.config(text=tick)


def reset_button():
    window.after_cancel(timer)
    global rep, tick
    rep = 0
    tick = ""
    ticks.config(text=tick)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="TIMER", fg=GREEN)


def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = "0"+str(count_sec)

    if len(str(count_min)) == 1:
        count_min = "0"+str(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()


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
timer_text = canvas.create_text(
    200, 170, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# start button

start = tkinter.Button(text="start", command=start_timer, bg="white")
start.grid(column=0, row=2)

# ticks label to identify no of
ticks = tkinter.Label(fg=PINK, font=("Verdana", 20, "bold"))
ticks.grid(column=1, row=3)


# reset button

reset = tkinter.Button(text="reset", command=reset_button, bg="white")
reset.grid(column=2, row=2)


window.mainloop()
