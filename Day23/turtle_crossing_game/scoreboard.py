from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 0
        self.update_scorebord()

    def update_scorebord(self):
        self.write(f"level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scorebord()

    def game_lost(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
