from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
score = 0
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.score_update(score)

screen.listen()
screen.onkeypress(fun=snake.up, key="w")
screen.onkeypress(fun=snake.down, key="s")
screen.onkeypress(fun=snake.right, key="d")
screen.onkeypress(fun=snake.left, key="a")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.clear()
        score += 1
        snake.extend()
        food.refresh()
        scoreboard.score_update(score)

    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -300 or snake.segment[0].ycor() > 300 or snake.segment[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for n in snake.segment:
        if n == snake.head:
            pass
        elif snake.head.distance(n) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()