from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def move(self):
        y_cor = self.ycor() + 10
        x_cor = self.xcor() + 10
        self.goto(x= x_cor, y= y_cor)