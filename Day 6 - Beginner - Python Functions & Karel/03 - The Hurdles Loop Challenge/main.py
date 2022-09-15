# This is for avoiding errors

def turn_left():
    reeborg = function

def move():
    reeborg = function

# Code starts from here

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for n in range(1,7):
    n = jump()