from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(height= 600, width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkeypress(r_paddle.up, "i")
screen.onkeypress(r_paddle.down, "k")
screen.onkeypress(l_paddle.up, "e")
screen.onkeypress(l_paddle.down, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    if ball.ycor() > 280:
        game_is_on = False


screen.exitonclick()