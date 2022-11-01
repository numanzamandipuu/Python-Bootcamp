from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid= 5, stretch_len=1)
        self.goto(position)


    def up(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + 20
        self.goto(x= x_cor, y= y_cor)

    def down(self):
        x_cor = self.xcor()
        y_cor = self.ycor() - 20
        self.goto(x= x_cor, y= y_cor)
