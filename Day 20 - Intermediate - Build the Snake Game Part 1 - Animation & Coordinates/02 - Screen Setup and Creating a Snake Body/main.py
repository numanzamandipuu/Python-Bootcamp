from turtle import Turtle, Screen

screen = Screen()
screen.title("My Snake Game")
screen.bgcolor("black")
screen.setup(height=600, width=600)


for i in range(3):
    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    tim.goto(x=(-20 * i), y=0)


screen.exitonclick()