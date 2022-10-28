from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()

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

        self.segment[0].forward(MOVE_DISTANCE)

        if self.segment[0].xcor() > 280:
            game_is_on = False