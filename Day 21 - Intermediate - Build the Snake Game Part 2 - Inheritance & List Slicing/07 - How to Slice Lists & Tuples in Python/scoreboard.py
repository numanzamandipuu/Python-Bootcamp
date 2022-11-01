from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")

    def score_update(self, score):
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)