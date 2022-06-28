from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class FirstToFive(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 270)
        self.hideturtle()

    def first_to_five(self):
        self.write("First to 5 Wins", False, align=ALIGNMENT, font=FONT)

    def player_1_win(self):
        self.setposition(0, -20)
        self.write("Player 1 Won!", False, align=ALIGNMENT, font=FONT)

    def player_2_win(self):
        self.setposition(0, -20)
        self.write("Player 2 Won!", False, align=ALIGNMENT, font=FONT)
