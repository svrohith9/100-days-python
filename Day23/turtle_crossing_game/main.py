import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager

scn = Screen()
scn.setup(width=600, height=600)
scn.tracer(0)
gamer = Player()
cars = CarManager()

scn.listen()
scn.onkey(gamer.go_up, "Up")
scn.onkey(gamer.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scn.update()
    cars.create_cars()
    cars.move_cars()
