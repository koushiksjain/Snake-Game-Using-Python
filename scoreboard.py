from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"My score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increasescore(self):
        self.score +=1
        self.clear()
        self.update()

    def increasescore5(self):
        self.score += 5
        self.clear()
        self.update()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

