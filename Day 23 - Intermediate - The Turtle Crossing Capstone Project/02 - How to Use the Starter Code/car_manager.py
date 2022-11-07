from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.forward(STARTING_MOVE_DISTANCE)
        

    def new_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.turtlesize(stretch_len= 2, stretch_wid= 1)
        new_car.y_axis = random.randint(-250, 250)
        new_car.goto(x= 150, y= new_car.y_axis)
        new_car.setheading(180)
        self.car_list.append(new_car)
