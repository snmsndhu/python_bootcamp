#Snake Game

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)







is_game_on = True

while is_game_on:
    screen.update()
    for seg_num in range(len(segements) - 1, 0, -1):
        new_x = segements[seg_num - 1].xcor()
        new_y = segements[seg_num - 1].ycor()
        segements[seg_num].goto(new_x, new_y)
    segements[0].forward(20)
    segements[0].left(90)


screen.exitonclick()