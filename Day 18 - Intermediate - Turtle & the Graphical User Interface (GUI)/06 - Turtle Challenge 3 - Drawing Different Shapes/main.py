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


###### identical source code start ######

# import turtle as t
# import random

# tim = t.Turtle()
# colors = ["navy", "yellow", "firebrick", "magenta", "purple", "red", "blue", "black", "green", "indigo"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(n)

###### identical source code end ######