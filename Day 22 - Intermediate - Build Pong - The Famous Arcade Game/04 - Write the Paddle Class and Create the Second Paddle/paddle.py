from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid= 5, stretch_len=1)
        self.up()


    def up(self):
        ycor_up = self.position()[1] + 20
        x_cor = self.position()[0]
        self.goto(x= x_cor, y= ycor_up)

    def down(self):
        ycor_up = self.position()[1] - 20
        x_cor = self.position()[0]
        self.goto(x= x_cor, y= ycor_up)
