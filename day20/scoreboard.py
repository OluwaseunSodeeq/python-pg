from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} highScore: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.update_highscore()
        self.score = 0
        self.update_scoreboard()

    def read_highscore(self):
        with open("data.txt") as file:
           return  int(file.read())

    def update_highscore(self):
        with open("data.txt", mode="w") as file:
           file.write(f"{self.highest_score}")
