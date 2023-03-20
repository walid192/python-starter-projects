from turtle import Turtle
import turtle


class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(x_cor,y_cor)
        
        
        
    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)        