from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

if user_bet:
    is_race_on = True

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-240, y=((i * 30) - 70))
    turtles.append(tim)

while is_race_on:
    forward = random.randint(0, 10)

    n = random.randint(0, 5)
    tim = turtles[n]
    tim.forward(forward)

    if tim.xcor() > 220:
        is_race_on = False

single_color = tim.color()
turtle_color = single_color[0]

if turtle_color == user_bet:
    print(f"You've won! The {turtle_color} turtle is the winner!")
else:
    print(f"You've lost! The {turtle_color} turtle is the winner!")


screen.exitonclick()