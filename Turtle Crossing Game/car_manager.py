from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

NUMBER_OF_CARS = 20


class CarManager:
    def __init__(self):

        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

        self.create_car()


    def create_car(self):
        random_chance = random.randint(1,6)
        
        if random_chance == 6:
            # Creating a Car
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=None, stretch_len=2, outline=None)
            car.goto(300, random.randint(-250,250))
            car.setheading(180)

            self.all_cars.append(car)
    

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    

    def level_up(self):
        self.car_speed += MOVE_INCREMENT




