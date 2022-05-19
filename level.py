from turtle import Turtle


class Level(Turtle):
    def __init__(self, co):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(co)
        self.hideturtle()
        self.Level()

    def Level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=('Arial', 16, 'normal'))

    def level_inc(self):
        self.level += 1
        self.Level()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\nScore: {self.level}", align = "center", font = ("Arial", 25, "bold"))

