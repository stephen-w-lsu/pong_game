from turtle import Turtle

UP = 90
DOWN = 270
PADDLE_LEN = 4
FWD_DISTANCE = 20

class Paddle2():

    def __init__(self):
        self.seg_list = []
        self.create_paddle()
        self.head = self.seg_list[0]
        self.tail = self.seg_list[-1]

    def create_paddle(self):
        x = 560
        y = 40
        for i in range(PADDLE_LEN):
            self.add_segment(x, y)
            y -= 20

    def add_segment(self, x_cor, y_cor):
        self.seg = Turtle("square")
        self.seg.color("white")
        self.seg.setheading(UP)
        self.seg.penup()
        self.seg.speed("slow")
        self.seg.goto(x_cor, y_cor)
        self.seg_list.append(self.seg)

    def up(self):
        for seg in self.seg_list:
            seg.setheading(UP)
            seg.forward(FWD_DISTANCE)

    def down(self):
        for seg in self.seg_list[::-1]:
            seg.setheading(DOWN)
            seg.forward(FWD_DISTANCE)
