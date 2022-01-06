from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.penup()
        self.color("black")
        self.goto(-280, 270)
        self.hideturtle()
        self.update_lvl()

    def update_lvl(self):
        self.write(f"Level: {self.lvl}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_lvl(self):
        self.lvl += 1
        self.clear()
        self.update_lvl()
