import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

i = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tim = Player()
car = CarManager()

screen.onkeypress(fun=tim.up, key="w")
screen.onkeypress(fun=tim.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    i += 1


    car.car_move()
    car.new_car()


screen.exitonclick()