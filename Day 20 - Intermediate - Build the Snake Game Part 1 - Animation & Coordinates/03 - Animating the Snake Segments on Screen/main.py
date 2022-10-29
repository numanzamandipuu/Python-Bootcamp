from turtle import Turtle, Screen
import time

screen = Screen()
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(height=600, width=600)
tim_list = []

for i in range(3):
    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    tim.goto(x=(-20 * i), y=0)
    tim_list.append(tim)

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    for n in range(len(tim_list) - 1, 0, -1):
        new_x = tim_list[n - 1].xcor()
        new_y = tim_list[n - 1].ycor()
        tim_list[n].goto(new_x, new_y)

    tim_list[0].forward(20)

    if tim_list[0].xcor() > 280:
        game_is_on = False
        

screen.exitonclick()