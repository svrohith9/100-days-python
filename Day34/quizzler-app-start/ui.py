from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Question", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        cross_image = PhotoImage(
            file=".\\Day34\\quizzler-app-start\\images\\false.png"
        )
        self.cross_button = Button(image=cross_image, highlightthickness=0)
        self.cross_button.grid(row=2, column=0)

        true_image = PhotoImage(
            file=".\\Day34\\quizzler-app-start\\images\\true.png"
        )
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=1)
        self.window.mainloop()
