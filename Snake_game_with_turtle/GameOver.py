from turtle import Turtle
ALIGNEMENT="center"
FONT=("Courier",24,"normal")

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.write("Game Over :(",True,ALIGNEMENT,FONT)
        self.hideturtle()
        