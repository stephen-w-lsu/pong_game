from turtle import Turtle

class Court(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=300)
        self.setheading(270)
        self.speed("fastest")
        self.pendown()

    def draw_dash(self):
        while self.ycor() != -300:
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()

    def draw_court(self):
        self.pendown()
        self.setheading(180)
        self.forward(600)
        self.setheading(90)
        self.forward(600)
        self.setheading(0)
        self.forward(1200)
        self.setheading(270)
        self.forward(600)
        self.setheading(180)
        self.forward(600)