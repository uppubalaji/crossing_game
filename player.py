from turtle import Turtle
from random import randint


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(0.8)
        self.setheading(90)
        self.goto(randint(-275, 275), -225)

    def respos(self):
        self.goto(randint(-275, 275), -225)

    def movu(self):
        self.forward(10)

    def movd(self):
        if self.ycor() > -225:
            self.backward(10)

    def movr(self):
        if self.xcor() < 275:
            self.setheading(0)
            self.forward(10)
            self.setheading(90)

    def movl(self):
        if self.xcor() > -275:
            self.setheading(180)
            self.forward(10)
            self.setheading(90)


