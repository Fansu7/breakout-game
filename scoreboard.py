from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(100, 425)
        self.score = score
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("arial", 10, "bold"))

    def score_point(self):
        self.score += 1
        self.print_score()

    def final_score(self):
        self.goto(0, 0)
        self.write(f"Final score: {self.score}", align="center", font=("arial", 40, "bold"))


class Lives(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(-100, 425)
        self.lives = lives
        self.print_lives()

    def print_lives(self):
        self.clear()
        self.write(f"Lives: {self.lives}", align="center", font=("arial", 10, "bold"))

    def lose_life(self):
        self.lives -= 1
        self.print_lives()
