from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
        

screen.exitonclick()