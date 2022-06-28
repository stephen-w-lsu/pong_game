from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(x, y)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()