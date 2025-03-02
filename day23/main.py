# The main.py file is responsible for bringing all the classes together and running the game. It creates an instance of each class and uses the methods of each class to run the game.
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player: Responsible for creating the player and controlling the player's movement.
player = Player()
# CarManager: Responsible for creating the cars and moving the cars.
car_manager = CarManager()
# Scoreboard: Responsible for keeping track of the level and displaying the level on the screen.
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

def start_crossing_again():
    player.goto(0, -280)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.randomly_create_car()
    car_manager.move_cars()

   # Detect collision with car
    for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

    # Detect when player reaches the top edge of the screen
    if player.is_at_finish_line():
        player.go_to_starting_position()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()