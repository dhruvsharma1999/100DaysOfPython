from turtle import Turtle, Screen
from D12_paddle import Paddle
from D12_ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('My pong game')
screen.tracer(0)


r_paddle = Paddle((380,0))
l_paddle = Paddle((-380,0))
ball = Ball()




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()



screen.exitonclick()