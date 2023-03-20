from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        
        
        
        
    def move(self):
        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
        
    def move_left(self):
        new_x=self.xcor()-MOVE_DISTANCE
        self.goto(new_x,self.ycor())
    
    def move_right(self):
        new_x=self.xcor()+MOVE_DISTANCE
        self.goto(new_x,self.ycor())
        
    def is_at_finish(self):
        return self.ycor()>280
    
    def reset_game(self):
        self.goto(STARTING_POSITION)
        
        
        
