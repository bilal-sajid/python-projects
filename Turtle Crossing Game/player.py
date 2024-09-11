
from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

NORTH = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.setheading(NORTH)

        self.penup()
        self.next_screen()
    
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    
    def next_screen(self):
        self.goto(STARTING_POSITION)