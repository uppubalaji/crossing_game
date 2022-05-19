from turtle import Turtle, Screen
from player import Player
from level import Level
from cars import Cars
from time import sleep


screen = Screen()
screen.setup(600, 500)
screen.tracer(0)

car = []
lev = Level((-250, 200))
player = Player()
cars = Cars()

screen.listen()
screen.onkey(player.movu, "Up")
screen.onkey(player.movd, "Down")
screen.onkey(player.movl, "Left")
screen.onkey(player.movr, "Right")

game_over = False
while not game_over:
    screen.update()
    sleep(0.1)
    cars.car1()
    cars.move()
    for i in cars.car:
        if player.distance(i) < 15:
            lev.game_over()
            game_over = True

    if player.ycor() > 230:
        player.respos()
        cars.lev_up()
        lev.level_inc()





screen.exitonclick()