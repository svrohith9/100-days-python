import tkinter

window = tkinter.Tk()
window.title("Miles to KM")
window.minsize(height=100, width=150)
window.config(padx=50, pady=75)


def miles_kms():
    ans = float(miles.get()) * 1.61
    kms.config(text=f"{round(ans,2)}")


# input placeholder miles
miles = tkinter.Entry(width=10)
miles.grid(column=1, row=0)

# label miles
display_text = tkinter.Label(text="Miles")
display_text.grid(column=2, row=0)

# output placeholder kms
kms = tkinter.Label(text="0")
kms.grid(column=1, row=1)

# label kms
display_text = tkinter.Label(text="Kms")
display_text.grid(column=2, row=1)

# label
display_text = tkinter.Label(text="equals to")
display_text.grid(column=0, row=1)

# button
calc = tkinter.Button(text="calculate", command=miles_kms)
calc.grid(column=1, row=3)


window.mainloop()