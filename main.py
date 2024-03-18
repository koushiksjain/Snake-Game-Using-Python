import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,  height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

gameon = True
while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if food.set_random_size() == (1.5, 1.5) or food.set_random_size() == (0.5, 0.5):
        food.refresh()
        snake.extend()
        scoreboard.increasescore()
# detect collisions
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increasescore()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameon = False
        scoreboard.gameover()
    #detect collisions with tail
    for snakes in snake.snakes[1:]:
        if snake.head.distance(snakes) <10:
            gameon = False
            scoreboard.gameover()












screen.exitonclick()