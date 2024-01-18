##More Turtle Graphics, Event Listeners, State and Multiple Instances

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()