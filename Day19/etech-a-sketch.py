from turtle import Turtle, Screen

t = Turtle()
scn = Screen()


def move_forward():
    t.forward(10)


def move_left():
    t.left(15)


def move_right():
    t.right(15)


def move_back():
    t.backward(10)


def clear_the_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


scn.listen()
scn.onkey(key="w", fun=move_forward)
scn.onkey(key="a", fun=move_left)
scn.onkey(key="d", fun=move_right)
scn.onkey(key="s", fun=move_back)
scn.onkey(key="c", fun=clear_the_screen)
scn.exitonclick()
