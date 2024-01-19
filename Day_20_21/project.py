#Snake Game

from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)


snake = Snake()





is_game_on = True

while is_game_on:
    screen.update()



screen.exitonclick()