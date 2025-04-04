
from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
Move_distance = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # self.penup()

    def create_snake (self):
        for each_position in STARTING_POSITION:
            self.add_segment(each_position)


    def add_segment(self, position):
        my_segment = Turtle("square")
        my_segment.color("white")
        my_segment.penup()
        my_segment.goto(position)
        self.segments.append(my_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for each_segment in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[each_segment- 1].xcor ()
            new_y= self.segments[each_segment- 1].ycor()
            self.segments[each_segment].goto(new_x, new_y)
            # each_segment.forward(20)
        self.head.forward(Move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        self.head.setheading(UP)
    def down (self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]