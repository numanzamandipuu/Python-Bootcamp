from turtle import Turtle, Screen, forward

tim = Turtle()

for i in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()