from turtle import *
import random

timmy = Turtle()
# Turtle.colormode(255)

# def randomColor():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color

timmy.speed("fastest")

for _ in range(200):
    # timmy.color(randomColor())
    timmy.circle(100)
    currnt_headin = timmy.heading()
    currnt_headin += 5
    timmy.setheading(currnt_headin)
    timmy.circle(100)
    
r












screen = Screen()
screen.exitonclick()

