import random
from turtle import Turtle, Screen
from player import Player
from ball import Ball
import time
from score_board import Scoreboard

scn = Screen()
scn.bgcolor("black")
scn.setup(width=800, height=600)
scn.title("Pong")
scn.tracer(0)  # remove default square animation

left_player = Player((-380, 0))
right_player = Player((380, 0))
ball = Ball()
score = Scoreboard()

scn.listen()
scn.onkey(right_player.go_up, "Up")
scn.onkey(right_player.go_down, "Down")
scn.onkey(left_player.go_up, "w")
scn.onkey(left_player.go_down, "s")

game_over = False

while not game_over:
    time.sleep(ball.ball_speed)
    scn.update()
    ball.move()

    # Detect Upper and Lower wall collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # detect collision with players
    if ball.xcor() > 360 and ball.distance(right_player.player) < 50 or ball.xcor() < -360 and ball.distance(left_player.player) < 50:
        ball.bounce_player()
        ball.ball_speed *= 0.9  # increase the speed of the ball after each touch

    if ball.xcor() > 400:
        ball.reset_postion()
        score.left_score()
        ball.ball_speed = 0.1
    if ball.xcor() < -400:
        ball.reset_postion()
        score.right_score()
        ball.ball_speed = 0.1


scn.exitonclick()
