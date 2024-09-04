from turtle import Turtle


class Ball(Turtle):
    def __init__(self, paddle_x, paddle_y):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.x = paddle_x
        self.y = paddle_y + 20
        self.goto(self.x, self.y)
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset(self, paddle_x, paddle_y):
        self.goto(paddle_x, paddle_y)

