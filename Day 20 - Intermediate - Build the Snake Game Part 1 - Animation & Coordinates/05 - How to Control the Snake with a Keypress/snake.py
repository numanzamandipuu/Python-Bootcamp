from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]


    def create_snake(self):
        for i in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(x=(-20 * i), y=0)
            self.segment.append(tim)


    def move(self):
        for n in range((len(self.segment) - 1), 0, -1):
            new_x = self.segment[n - 1].xcor()
            new_y = self.segment[n - 1].ycor()
            self.segment[n].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if int(self.head.heading()) == 270:
            pass
        else:
            self.head.setheading(UP)

    def down(self):
        if int(self.head.heading()) == 90:
            pass
        else:
            self.head.setheading(DOWN)

    def left(self):
        if int(self.head.heading()) == 0:
            pass
        else:
            self.head.setheading(LEFT)

    def right(self):
        if int(self.head.heading()) == 180:
            pass
        else:
            self.head.setheading(RIGHT)