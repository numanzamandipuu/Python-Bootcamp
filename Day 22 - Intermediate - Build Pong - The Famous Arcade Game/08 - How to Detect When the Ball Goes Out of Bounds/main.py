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
    time.sleep(0.05)


    ball.move()

    if r_paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.ycor() == 400:
        game_is_on = False


screen.exitonclick()