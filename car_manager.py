from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5
MOVE_DISTANCE = 5
PROBABILITY_RANGE = 5


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(0, PROBABILITY_RANGE) == 0:
            new_car = Car()
            self.all_cars.append(new_car)
            self.move_distance = MOVE_DISTANCE

    def move(self):
        for _ in self.all_cars:
            _.goto(_.xcor()-self.move_distance, _.ycor())

    def reset_car(self):
        for _ in self.all_cars:
            if _.xcor() < -300:
                _.reset()

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.activated = False
        self.reset()

    def reset(self):
        self.hideturtle()
        self.color(COLORS[random.randint(0, 5)])
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(400, random.randint(-240, 300))
        self.activated = True
        self.showturtle()
