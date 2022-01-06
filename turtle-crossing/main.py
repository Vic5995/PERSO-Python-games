import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle race")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.generate_cars()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    if player.is_on_top():
        player.go_to_start()
        score_board.increase_lvl()
        car_manager.lvl_up()

screen.exitonclick()
