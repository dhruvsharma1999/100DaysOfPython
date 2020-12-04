from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    
    tim.backward(10)

def move_c_clock():

    tim.left(10)

def clock():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown
    
screen.listen()
screen.onkey(key="d", fun=move_forward)
screen.onkey(key="a", fun=move_backward)
screen.onkey(key="w", fun=move_c_clock)
screen.onkey(key="s", fun=clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
