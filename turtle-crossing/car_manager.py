import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        # self.create_cars()

    # def create_cars(self):
    #     for _ in range(0, 20):
    #         self.new_car(random.randint(-300, 300))

    def generate_cars(self):
        rand = random.randint(1, 5)
        if rand == 1:
            # self.new_car(300)
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    # def new_car(self, x_pos):
    #     car = Turtle("square")
    #     car.shapesize(stretch_len=2, stretch_wid=1)
    #     car.penup()
    #     car.color(random.choice(COLORS))
    #     car.goto(x_pos, random.randint(-250, 250))
    #     self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT


