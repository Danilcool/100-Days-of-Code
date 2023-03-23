from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
car_dificulty = [1,2,3,4,5,6,7]
SPEED = 6

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []



    def create_car(self):
        random_chance_per_car = random.choice(car_dificulty)
        if random_chance_per_car == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.speed(SPEED)
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)

    def increase_level(self):
        car_dificulty.append(1)


