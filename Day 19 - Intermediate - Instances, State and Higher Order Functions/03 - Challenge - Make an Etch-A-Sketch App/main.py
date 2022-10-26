from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

def w():
    tim.forward(10)

def s():
    tim.backward(10)

def a():
    tim.left(10)

def d():
    tim.right(10)

def c():
    screen.resetscreen()
    tim.goto(0, 0)


screen.onkeypress(w, "w")
screen.onkeypress(s, "s")
screen.onkeypress(a, "a")
screen.onkeypress(d, "d")
screen.onkeypress(c, "c")

screen.exitonclick()