from turtle import Turtle, Screen

right_tim = Turtle()
screen = Screen()


def right_tim_up():
    right_tim.forward(20)

def right_tim_down():
    right_tim.forward(-20)


screen.setup(height= 600, width= 800)
screen.bgcolor("black")
screen.title("Pong")


right_tim.goto(x= 350, y=0)
right_tim.shape("square")
right_tim.penup()
right_tim.color("white")
right_tim.turtlesize(stretch_wid= 5, stretch_len=1)


screen.listen()
screen.onkeypress(right_tim_up, "i")
screen.onkeypress(right_tim_down, "k")


screen.exitonclick()