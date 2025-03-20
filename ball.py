from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.shapesize()
        
    def move_right_up(self):
       x_cor = self.xcor()
       y_cor = self.ycor()
       self.goto(x_cor + 10, y_cor + 10)
    #    if(x_cor >= 350 or y_cor >= 300):
    #        pass
    #    else:
      