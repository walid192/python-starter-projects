from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.write(f"Level : {self.level}",True,"left",FONT)
        
    def increase_level(self):
        self.level+=1
        self.clear()
        self.penup()
        self.goto(-280,250)
        self.write(f"Level : {self.level}",True,"left",FONT)
    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write("Game over",True,"center",FONT)
