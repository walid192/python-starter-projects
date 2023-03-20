from random import choice, randint
from turtle import Turtle
import turtle



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars=[]
        self.car_speed=MOVE_INCREMENT
        
       
        
        
    def CreateCar(self):
        if randint(1,6)==6:
            
            car=Turtle("square")
            car.shapesize(1,2)
            car.color(choice(COLORS))
            rand_y=randint(-250,250)
            car.penup()
            car.goto(260,rand_y)
            self.cars.append(car)
        
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
        
        
    
