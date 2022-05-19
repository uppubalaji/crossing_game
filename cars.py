from turtle import Turtle, colormode
from random import randint


colormode(255)
class Cars:
    def __init__(self):
        self.car = []
        self.sp = 5

    def car1(self):
        chance = randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(0.75, 1.75)
            new_car.color(randint(1, 255),
                       randint(1,255),
                       randint(1,255))
            new_car.penup()
            new_car.goto(randint(325, 750), randint(-200, 200))
            self.car.append((new_car))

    def move(self):
        for i in self.car:
            i.backward(self.sp)

    def lev_up(self):
        self.sp += 5

