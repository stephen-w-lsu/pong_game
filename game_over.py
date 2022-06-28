from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(0, 20)
        self.hideturtle()

    def game_over(self):
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)