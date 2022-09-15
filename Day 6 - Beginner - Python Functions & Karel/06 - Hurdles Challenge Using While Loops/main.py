# This is for avoiding errors

def turn_left():
    reeborg = function

def move():
    reeborg = function

def at_goal():
    reeborg = function

def front_is_clear():
    reeborg = function

# Code starts from here

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()