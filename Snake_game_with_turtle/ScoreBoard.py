from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(365,365)
        self.write(f"Score :{self.score}",True,"right",("arial",24,"normal"))
        
        self.hideturtle()
        
        
    def Increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score :{self.score}",True,"right",("arial",24,"normal"))

        

        
        