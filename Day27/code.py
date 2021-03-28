from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("Tkinter GUI")
window.minsize(width=600, height=400)
window.config(padx=300, pady=200)

# label
my_label = Label(text="This is label ")
my_label.grid(column=0, row=0)

# Input Field

data_input = Entry(width="20")
data_input.grid(column=0, row=3)


def button_clicked():
    print("clicked")
    my_label.config(text=data_input.get())


# button
button = Button(text="okay", command=button_clicked)
button.grid(column=0, row=4)


window.mainloop()
