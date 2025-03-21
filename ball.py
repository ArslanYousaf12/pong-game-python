from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        
        # self.shapesize()
        
    def move(self):
       x_cor = self.xcor()
       y_cor = self.ycor()
       self.goto(x_cor + self.x_move, y_cor + self.y_move)
       
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
        
    def restart(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()

        
             
       
    #    if(x_cor >= 350 or y_cor >= 300):
    #        pass
    #    else:
      