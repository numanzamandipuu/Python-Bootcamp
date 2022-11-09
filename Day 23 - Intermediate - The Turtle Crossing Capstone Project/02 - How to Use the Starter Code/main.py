import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


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
    
 



screen.exitonclick()
