from turtle import Turtle, Screen

tim = Turtle()

num_sides = 3

while num_sides < 11:

    for n in range(num_sides):
        tim.forward(100)
        tim.right(360 / num_sides)
        
    num_sides += 1

screen = Screen()
screen.exitonclick()