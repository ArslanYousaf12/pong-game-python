from turtle import  Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width= 800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
speed = 8
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    
    # # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330 :
        ball.bounce_x()
        
    
    # R paddle misses the ball
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()
    # L paddle misses the ball
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()
      


screen.exitonclick()