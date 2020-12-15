FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)