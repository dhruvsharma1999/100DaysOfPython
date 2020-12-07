from turtle import Turtle, Screen
import random
# timy = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
y_index = -100
all_turtle =[]
for turtle_index in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_index)
    y_index += 40
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:


    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've have won! The {win_color} turtle is the winner!")
            else:
                print(f"You've have lost! The {win_color} turtle is the winner!")
        random_dist = random.randint(0,10)
        turtle.forward(random_dist)

screen.exitonclick()