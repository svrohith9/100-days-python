from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open(".\\100-days-python\\Day20_Day21\\score_data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scorecard()

    def update_scorecard(self):
        self.clear()
        self.write(
            f"Score : {self.score} | High Score {self.high_score}", align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(".\\100-days-python\\Day20_Day21\\score_data.txt", mode='w') as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scorecard()

    def increase_score(self):
        self.score += 1
        self.update_scorecard()
