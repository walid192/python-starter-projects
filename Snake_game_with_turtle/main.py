import time
from turtle import Screen, Turtle, pos
from ScoreBoard import ScoreBoard
from GameOver import GameOver
from food import Food

from snake import Snake

screen=Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake=Snake()
food=Food()
scoreBoard=ScoreBoard()

screen.listen()
screen.onkey(snake.up ,"Up ")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left  ,"Left")
screen.onkey(snake.right ,"Right")

Game_is_on=True
while Game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    
    #detecting collisions with food
    position=snake.segments[0].position()
    if food.distance(position)<15:
        food.refresh()
        snake.Add_Segment()
        scoreBoard.Increase_score()
        
        
        
    #detecting collisions with walls
    if (abs(snake.segments[0].xcor())==400) or (abs(snake.segments[0].ycor())==400):
        game_over=GameOver()
        Game_is_on=False    
        
        
    #detect collision with tail
    for segment in snake.segments:
        if segment==snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment)<10:
            Game_is_on=False
            game_over=GameOver()    
      
    
    
    

















screen=Screen()
screen.exitonclick()