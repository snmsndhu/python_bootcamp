#Etch A Sketch Exercise

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

screen.listen()
screen.onkey(key="w", fun= move_forward)
screen.onkey(key="s", fun=move_backward)
screen.exitonclick()