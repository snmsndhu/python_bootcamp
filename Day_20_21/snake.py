from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segements = []
        self.create_snake()
        self.head = self.segements[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segements.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segements) - 1, 0, -1):
            new_x = self.segements[seg_num - 1].xcor()
            new_y = self.segements[seg_num - 1].ycor()
            self.segements[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)
    def left(self):

        self.head.setheading(180)

    def right(self):

        self.head.setheading(90)
