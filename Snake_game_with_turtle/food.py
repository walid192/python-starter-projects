from random import randint, random
import turtle


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.penup()
        self.refresh()
        
    
        
        
        
    def refresh(self):
        self.rand_x=randint(-280,280)
        self.rand_y=randint(-280,280)
        self.goto(self.rand_x,self.rand_y)
        