from turtle import Turtle, Screen

from player import Player
from scoreboard import Scoreboard
from car import Car
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Racing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = Car()

screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_successful():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()