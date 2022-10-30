from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")

    def score_update(self, score):
        self.write(arg=f"Score: {score}", align="center", font=("Arial", 16, "bold"))