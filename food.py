from turtle import Turtle
import random
colors = []

for i in range(50):
    colors.append('#%06X' % random.randint(0, 0xFFFFFF))

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def set_random_size(self):
        stretch_len = random.uniform(0.5, 1.5)  # Random stretch length between 0.5 and 1.5
        stretch_wid = random.uniform(0.5, 1.5)  # Random stretch width between 0.5 and 1.5
        self.shapesize(stretch_len, stretch_wid)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.color(random.choice(colors))


