from turtle import Turtle
import random

FWD_DISTANCE = 20
INITIAL_X = 0
INITIAL_Y = 0
START_ANGLE = []
for i in range(7, 45, 7):
    START_ANGLE.append(i)
for i in range(135, 225, 7):
    START_ANGLE.append(i)
for i in range (315, 350, 7):
    START_ANGLE.append(i)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.setposition(INITIAL_X, INITIAL_Y)


    def random_start(self):
        self.setposition(INITIAL_X, INITIAL_Y)
        self.setheading(random.choice(START_ANGLE))

    def move(self):
        self.forward(FWD_DISTANCE)

    def up_even_turn(self):
        self.setheading(180 - self.heading())
        self.move()

    def down_turn(self):
        self.setheading(540 - self.heading())
        self.move()

    def top_bot_turn(self):
        self.setheading(360 - self.heading())
        self.move()
