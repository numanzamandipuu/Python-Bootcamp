# This is for avoiding errors

def turn_left():
    reeborg = function

def move():
    reeborg = function

def at_goal():
    reeborg = function

def front_is_clear():
    reeborg = function

def wall_on_right():
    reeborg = function

# Code starts from here

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right() and front_is_clear():
        move()
    if not front_is_clear():
        turn_left()
        
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()