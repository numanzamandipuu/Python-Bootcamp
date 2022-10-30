from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.turtlesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.speed(0)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x= random_x, y= random_y)
