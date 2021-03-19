from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

segments = []

scn = Screen()
scn.setup(width=600, height=600)
scn.bgcolor("black")
scn.title("Nokia Snake Game")
scn.tracer(0)

snake = Snake()
food = Food()

scn.listen()
scn.onkey(snake.up, "Up")
scn.onkey(snake.down, "Down")
scn.onkey(snake.left, "Left")
scn.onkey(snake.right, "Right")

game_on = True
while game_on:
    scn.update()
    time.sleep(0.1)
    snake.move()

    # detect if food consumed
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
    # detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = False

scn.exitonclick()
