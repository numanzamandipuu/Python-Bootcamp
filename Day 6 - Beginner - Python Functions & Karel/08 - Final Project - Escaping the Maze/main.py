# This is for avoiding errors

def turn_left():
    reeborg = function

def move():
    reeborg = function

def at_goal():
    reeborg = function

def front_is_clear():
    reeborg = function

def right_is_clear():
    reeborg = function

# Code starts from here

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()