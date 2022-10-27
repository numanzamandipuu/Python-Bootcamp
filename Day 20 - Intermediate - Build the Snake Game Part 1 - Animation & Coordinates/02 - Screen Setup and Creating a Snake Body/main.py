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


###### identical source code start ######

# from turtle import Turtle, Screen

# screen = Screen()
# screen.setup(height=600, width=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")

# starting_position = [(0, 0), (-20, 0), (-40, 0)]

# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)


# screen.exitonclick()

###### identical source code end ######