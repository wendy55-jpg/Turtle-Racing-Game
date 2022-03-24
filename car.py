from turtle import Turtle
import random
COLOURS = ("red", "orange", "blue", "purple", "red", "yellow", "green", "pink")

class Car:
    def __init__(self):
        self.all_cars =[]
        self.car_speed = 5

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLOURS))
            new_car.penup()
            random_y = random.randint(-220, 200)
            new_car.goto(400, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(5)

    def level_up(self):
        self.car_speed += 10


