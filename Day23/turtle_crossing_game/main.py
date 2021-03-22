import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager

scn = Screen()
scn.setup(width=600, height=600)
scn.tracer(0)
score = Scoreboard()
gamer = Player()
cars = CarManager()

scn.listen()
scn.onkey(gamer.go_up, "Up")
scn.onkey(gamer.go_down, "Down")


def hit_by_car():
    for car in cars.all_cars:
        if car.distance(gamer) < 20:
            return True
    return False


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scn.update()

    cars.create_cars()
    cars.move_cars()

    # check if turtle hit any car
    if hit_by_car():
        game_is_on = False
        score.game_lost()

    # detect turtle finished
    if gamer.goal_reached():
        gamer.goto_start()
        # update level
        cars.increase_speed()
        score.increase_level()


scn.exitonclick()
