from turtle import Turtle

ALIGNEMENT="center"
FONT=("Courier",18,"normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score=0
        self.right_score=0
        self.show_Score()
        
        
        
    def show_Score(self):
        self.goto(-100 ,200)
        self.write(f"{self.left_score}",True,ALIGNEMENT,FONT)
        self.goto(100 ,200)
        self.write(f"{self.right_score}",True,ALIGNEMENT,FONT)
        