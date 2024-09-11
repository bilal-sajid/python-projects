import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Event Listeners for player
screen.listen()
screen.onkey(player.move_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating and moving cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with Car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if player reached
    if player.ycor() == 280:
        player.next_screen()
        scoreboard.level_up()
        car_manager.level_up()


screen.exitonclick()
