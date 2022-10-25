from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.speed(0)
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


for i in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)

screen.exitonclick()