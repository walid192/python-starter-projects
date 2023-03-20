import time
from turtle import Screen, Turtle
from Ball import Ball
from ScoreBoard import ScoreBoard

from paddle import Paddle
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)


screen.listen()


l_paddle=Paddle(-380,0)
r_paddle=Paddle(380,0)

ball=Ball()
scoreboard=ScoreBoard()

screen.onkeypress(l_paddle.go_up,"a")
screen.onkeypress(l_paddle.go_down,"w")

screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

Game_is_on=True
while Game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    
    ball.move()
    
    #detect collision with wall
    if ball.ycor()<-300 or ball.ycor()>300:
        ball.bounce_y()
        
        
    #detect collision with paddle
    if ball.xcor()<-320 and ball.distance(l_paddle)<50 or ball.xcor()>320 and ball.distance(r_paddle)<50 :
        ball.bounce_x()
        
        
    #detect ball misses right paddle
    if ball.xcor()>390:
        ball.reset_position()
        scoreboard.left_score+=1
        scoreboard.clear()
        scoreboard.show_Score()
        
        
        
    #detect ball misses left paddle
    if ball.xcor()<-390:
        ball.reset_position()   
        scoreboard.right_score+=1
        scoreboard.clear()
        scoreboard.show_Score()
        
        
screen.exitonclick()