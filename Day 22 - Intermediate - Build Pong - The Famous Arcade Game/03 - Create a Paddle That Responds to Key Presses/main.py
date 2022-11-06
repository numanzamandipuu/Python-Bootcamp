from turtle import Turtle, Screen

paddle = Turtle()
screen = Screen()


def up():
    ycor_up = paddle.position()[1] + 20
    paddle.goto(x= 350, y= ycor_up)

def down():
    ycor_down = paddle.position()[1] - 20
    paddle.goto(x= 350, y= ycor_down)


screen.setup(height= 600, width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle.goto(x= 350, y=0)
paddle.shape("square")
paddle.penup()
paddle.color("white")
paddle.turtlesize(stretch_wid= 5, stretch_len=1)


screen.listen()
screen.onkeypress(up, "i")
screen.onkeypress(down, "k")


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()