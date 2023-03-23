import time
from player import Player
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()


screen.onkey(player.up,'w')
screen.onkey(player.down,'s')





game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            score_board.game_over()
            time.sleep(0.5)
            game_is_on = False

    #player crossing to the next level
    if player.ycor() > 290:
        score_board.score_up()
        player.starting_position()
        car_manager.increase_level()



