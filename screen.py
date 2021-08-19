from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING PONG Game")

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()
screen.tracer(0)
screen.update()
screen.listen()
screen.onkey(key="Up", fun=paddle1.up)
screen.onkey(key="Down", fun=paddle1.down)
screen.onkey(key="w", fun=paddle2.up)
screen.onkey(key="s", fun=paddle2.down)

game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if ball.xcor() > 320 and ball.distance(paddle1) < 50 or ball.xcor() < -320 and ball.distance(paddle2) < 50:
        ball.bounce_paddle()
    if ball.xcor() > 380:
        ball.reset()
        score.paddle1_score += 1
        score.update_scoreboard()
    if ball.xcor() < -380:
        ball.reset()
        score.paddle2_score += 1
        score.update_scoreboard()

screen.exitonclick()
