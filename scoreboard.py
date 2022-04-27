from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(200, -270)
        self.score = -1
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(130, -270)
        self.write(f"Game over! Score: {self.score}", align="center", font=FONT)