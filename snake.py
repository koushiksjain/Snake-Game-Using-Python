from turtle import Turtle

start = [(0, 0), (-20, 0), (-40, 0)]
movdis = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.createsnake()
        self.head = self.snakes[0]

    def createsnake(self):
        for pos in start:
            self.addsegment(pos)
            # snake = Turtle("square")
            # snake.color("white")
            # snake.penup()
            # snake.goto(pos)
            # self.snakes.append(snake)

    def addsegment(self, pos):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.snakes.append(snake)

    def extend(self):
        self.addsegment(self.snakes[-1].pos())
    def extend5(self):
        self.addsegment(self.snakes[-1].pos()+5)

    def move(self):
        for seg_mun in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg_mun - 1].xcor()
            new_y = self.snakes[seg_mun - 1].ycor()
            self.snakes[seg_mun].goto(new_x, new_y)
        self.head.forward(movdis)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
