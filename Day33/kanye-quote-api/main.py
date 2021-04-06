from tkinter import *
import requests


def get_quote():
    try:
        response = requests.get(url="http://api.kanye.rest")
    except UnboundLocalError:
        canvas.itemconfig(quote_text, text="Connection timed out")
    if response.status_code == 200:
        data = response.json()
        canvas.itemconfig(quote_text, text=data["quote"])
    else:
        canvas.itemconfig(quote_text, text="Content not found")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(
    file=".\\100-days-python\\Day33\\kanye-quote-api\\background.png"
)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 20, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=".\\100-days-python\\Day33\\kanye-quote-api\\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()