from turtle import Turtle, Screen
from score_board import Score_board
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Score_board()

screen.listen()

# up keys
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_up, "w")

# Down keys
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    # time.sleep(ball.move_speed)
    screen.update()
    ball.move()
   


    # Detect collision with wall
    if ball.ycor() < 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if  ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()
        # ball.bounce_x()

# Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()
        # ball.bounce_x()

screen.exitonclick()