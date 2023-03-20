from pickle import FALSE
import time
from turtle import Screen
from player import FINISH_LINE_Y
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player=Player()
scoreboard=Scoreboard()
car=CarManager()



screen.listen()
screen.onkeypress(player.move,"Up")
screen.onkeypress(player.move_left,"Left")
screen.onkeypress(player.move_right,"Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.CreateCar()
    car.move_cars()
    
    
    #detect collision with car
    for c in car.cars:
        if player.distance(c)<20:
            scoreboard.gameover()
            game_is_on=False
            
            
            
            
            
    #detect finish line
    if player.is_at_finish():
        player.reset_game()
        car.level_up()
        scoreboard.increase_level()
        
        
