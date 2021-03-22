from turtle import Turtle
base_positions = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, postion):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(postion)
        self.segments.append(segment)

    def create_snake(self):
        for postion in base_positions:
            self.add_segment(postion)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        # setting pos of dead snakes to 999,999
        for seg in self.segments:
            seg.goto(999, 999)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
