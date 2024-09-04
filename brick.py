from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2.5, stretch_wid=0.6)
        self.x = x
        self.y = y
        self.color(color)
        self.penup()
        self.goto(x, y)
