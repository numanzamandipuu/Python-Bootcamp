from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

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
        food.refresh()

    if snake.segment[0].xcor() > 280:
        game_is_on = False

screen.exitonclick()