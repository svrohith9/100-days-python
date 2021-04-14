from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width="250", text="Question", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        cross_image = PhotoImage(
            file=".\\Day34\\quizzler-app-start\\images\\false.png"
        )
        self.cross_button = Button(
            image=cross_image, highlightthickness=0, command=self.false_button)
        self.cross_button.grid(row=2, column=0)

        true_image = PhotoImage(
            file=".\\Day34\\quizzler-app-start\\images\\true.png"
        )
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.score_label.config(text=f"Score : {self.quiz.score}")

    def false_button(self):
        is_right = self.quiz.check_answer("false")
        self.response_feedback(is_right)

    def true_button(self):
        is_right = self.quiz.check_answer("true")
        self.response_feedback(is_right)

    def response_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
