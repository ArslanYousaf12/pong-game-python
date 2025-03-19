from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1,0)
        self.penup()
        self.goto(350, 0)
      
        # self.turtlesize(2,1,0)
   
          
        
    def up(self):
        paddle_position  = self.ycor()
        self.setposition(self.xcor(), paddle_position + 20)
        # self.center_position()
    
    def down(self):
        paddle_position  = self.ycor()
        self.setposition(self.xcor(), paddle_position - 20)
        # self.center_position()
        
    