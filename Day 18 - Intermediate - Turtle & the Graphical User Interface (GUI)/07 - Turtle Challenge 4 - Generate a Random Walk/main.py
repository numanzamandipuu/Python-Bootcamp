from turtle import Turtle, Screen
import random

colors = ["navy", "yellow", "firebrick", "magenta", "purple", "red", "blue", "black", "green", "indigo"]
tim = Turtle()
tim.pensize(10)
tim.speed(0)

def front():
    tim.forward(20)

def right():
    tim.right(90)

def left():
    tim.left(90)

def back():
    tim.right(180)

direction = [front, right, left, back]

for i in range(200):
    tim.color(random.choice(colors))
    function = random.choice(direction)
    function()
    tim.forward(20)

screen = Screen()
screen.exitonclick()