from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NEW_CAR = ["yes", "no"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.y_axis = random.randint(-250, 250)
        self.goto(x= 150, y= self.y_axis)
        self.turtlesize(stretch_len= 2, stretch_wid= 1)
        self.setheading(180)
        self.car_list = []

    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def new_car(self):
        self.y_axis = random.randint(-250, 250)
        self.goto(x= 150, y= self.y_axis)
