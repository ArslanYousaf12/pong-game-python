from turtle import  Screen
from paddle import Paddle
import time
from ball import Ball



screen = Screen()
screen.setup(width= 800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
   
    screen.update()
    ball.move_right_up()


screen.exitonclick()