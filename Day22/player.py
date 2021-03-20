from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.player = Turtle("square")
        self.player.shapesize(stretch_len=1, stretch_wid=5)
        self.player.color("white")
        self.player.penup()
        self.player.goto(position)

    def go_up(self):
        new_y = self.player.ycor()+20
        self.player.goto(self.player.xcor(), new_y)

    def go_down(self):
        new_y = self.player.ycor()-20
        self.player.goto(self.player.xcor(), new_y)
