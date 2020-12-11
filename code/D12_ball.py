from turtle import Turtle
import random 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_mov = 10
        self.y_mov = 10

    def move_ball(self):
        new_x  = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_mov *= -1