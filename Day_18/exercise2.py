#Turtle generating different shapes

from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["red", "yellow", "blue", "green"]

def generate_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)

for shapes in range(3, 11):
    tim.color(random.choice(colours))
    generate_shapes(shapes)



screen = Screen()
screen.exitonclick()