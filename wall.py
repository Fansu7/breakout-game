from turtle import Turtle


class Wall(Turtle):
    def __init__(self, position, turn):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=45)
        self.color("white")
        self.penup()
        self.left(turn)
        self.goto(position)