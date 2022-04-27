import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:

    #Make new car or reset car position
    if len(car_manager.all_cars) < 28:
        car_manager.create_car()

    car_manager.reset_car()
    car_manager.move()

    #Detect finish
    if player.finished():
        player.reset_position()
        car_manager.speed_up()
        scoreboard.increase_score()

    #Detect collision
    for _ in car_manager.all_cars:
        if _.activated and player.resetting == False \
                and player.xcor() > _.xcor()-30 and player.xcor() < _.xcor()+30\
                and player.ycor() > _.ycor()-20 and player.ycor() < _.ycor()+20:
            game_is_on = False
            scoreboard.game_over()

    #Slow down traffic once enough cars appear
    if len(car_manager.all_cars) > 25:
        time.sleep(0.1)

    screen.update()



screen.exitonclick()