from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("D:/Python-Bootcamp/Day 24 - Intermediate - Files, Directories and Paths/04 - Challenge - Read and Write the High Score to a File in Snake/data.txt", mode= "r") as file:
            high_score_int = int(file.read())
        self.high_score = high_score_int
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("D:/Python-Bootcamp/Day 24 - Intermediate - Files, Directories and Paths/04 - Challenge - Read and Write the High Score to a File in Snake/data.txt", mode= "w") as files:
                files.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()