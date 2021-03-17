from turtle import Turtle, Screen
import random

colors = ["purple", "red", "yellow", "green", "blue", "orange", "indigo"]
base_positions = [-75, -50, -25, 0, 25, 50, 75]
turtles = []

scn = Screen()
scn.setup(height=400, width=600)
user_input = scn.textinput(
    title="Choose a color", prompt="Which turtle will win the race? choose a rainbow color: ")


def create_turtle(y):
    t = Turtle(shape="turtle")
    t.color(colors[y])
    t.penup()
    t.goto(x=-275, y=base_positions[y])
    turtles.append(t)


def move_forward(turtles):

    for turtle in turtles:
        turtle.forward(random.randint(10, 15))
        if turtle.xcor() >= 270:
            print(f"{turtle.pencolor()} Won the Race")
            if turtle.pencolor() == user_input:
                print("You Won!")
            else:
                print("You Lost")
            return True


def start_race():
    game_over = False
    while not game_over:
        game_over = move_forward(turtles)


def start():
    t = 6
    while t >= 0:
        create_turtle(t)
        t -= 1
    if user_input:
        start_race()


start()

scn.exitonclick()
