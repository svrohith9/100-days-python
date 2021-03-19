from turtle import Turtle, Screen
import time

base_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

scn = Screen()
scn.setup(width=600, height=600)
scn.bgcolor("black")
scn.title("Nokia Snake Game")
scn.tracer(0)


for xy in base_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(xy)

    segments.append(segment)

game_on = True

while game_on:
    scn.update()
    time.sleep(0.3)

    for seg in range(len(segments)-1, 0, -1):
        new_x = segments[seg-1].xcor()
        new_y = segments[seg-1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

scn.exitonclick()
