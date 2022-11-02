from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height= 600, width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.up, "i")
screen.onkeypress(r_paddle.down, "k")
screen.onkeypress(l_paddle.up, "e")
screen.onkeypress(l_paddle.down, "d")


time_sleep = 0.05
game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(time_sleep)


    ball.move()

    if r_paddle.distance(ball) < 50 and ball.xcor() > 330 or l_paddle.distance(ball) < 50 and ball.xcor() < -330:

        if time_sleep > 0:
            time_sleep *= 0.9
        
        ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        scoreboard.r_increase()
        ball.reset_position()
        time_sleep = 0.05

    if ball.xcor() < -380:
        scoreboard.l_increase()
        ball.reset_position()
        time_sleep = 0.05


screen.exitonclick()