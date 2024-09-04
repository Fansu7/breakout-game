import random
from paddle import Paddle
from ball import Ball
from wall import Wall
from brick import Brick
from turtle import Screen
from scoreboard import Scoreboard, Lives


def main_game():

    def check_collision(bricks):
        for brick in bricks:
            if ball.distance(brick) < 40:
                ball.bounce_y()
                brick.goto(2000, 2000)
                scoreboard.score_point()

    def create_bricks():
        x = -355
        y = 400
        for i in range(0, 5):
            for j in range(0, 14):
                color = random.choice(colors)
                brick = Brick(x, y, color)
                bricks.append(brick)
                x += 55
            y -= 20
            x = -355

    colors = ["blue", "red", "green", "yellow", "pink", "white", "gray", "orange", "purple", "brown"]
    bricks = []
    score = 0
    lives_remaining = 3


    paddle = Paddle((0, -400))
    ball = Ball(paddle.xcor(), paddle.ycor()+35)

    wall_r = Wall((400, 0), 90)
    wall_l = Wall((-405, 0), 90)
    wall_up = Wall((0, 455), 0)

    scoreboard = Scoreboard(score)
    lives = Lives(lives_remaining)

    screen = Screen()
    screen.setup(width=800, height=900)
    screen.title("Breakout Game")
    screen.bgcolor("black")
    screen.tracer(0)
    paddle.left(90)
    screen.listen()
    screen.onkey(paddle.go_left, "a")
    screen.onkey(paddle.go_right, "d")

    create_bricks()

    game_on = True
    while game_on:
        screen.update()
        ball.move()

        if ball.xcor() >= 380 or ball.xcor() <= -380:
            ball.bounce_x()
        elif ball.ycor() >= 430:
            ball.bounce_y()
        elif ball.ycor() > -390 and (ball.distance(paddle) < 30):
            ball.bounce_y()
        elif ball.ycor() >= 300:
            check_collision(bricks)
        elif ball.ycor() < -450:
            ball.reset(paddle.xcor(), paddle.ycor()+20)
            ball.bounce_y()
            lives.lose_life()
            lives_remaining -= 1
            if lives_remaining == 0:
                scoreboard.final_score()
                game_on = False

    screen.mainloop()


main_game()
