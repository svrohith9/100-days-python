import random
from turtle import Turtle, Screen
from player import Player
from ball import Ball
import time


scn = Screen()
scn.bgcolor("black")
scn.setup(width=800, height=600)
scn.title("Pong")
scn.tracer(0)  # remove default square animation

left_player = Player((-380, 0))
right_player = Player((380, 0))
ball = Ball()

scn.listen()
scn.onkey(right_player.go_up, "Up")
scn.onkey(right_player.go_down, "Down")
scn.onkey(left_player.go_up, "w")
scn.onkey(left_player.go_down, "s")

game_over = False

while not game_over:
    time.sleep(0.1)
    scn.update()
    ball.move()

    # Detect Upper and Lower wall collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    print(ball.distance(right_player), " ", ball.xcor())
    # detect collision with players
    if ball.xcor() > 360 and ball.distance(right_player) < 50:
        ball.bounce_player()


scn.exitonclick()
