from turtle import  Screen
from paddle import Paddle
import time



screen = Screen()
screen.setup(width= 800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle()
screen.listen()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

is_game_on = True
while is_game_on:
    screen.update()


screen.exitonclick()