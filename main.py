from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_Is_Running = True
while game_Is_Running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    # if snake head is 15 pixels away from a 10x10 pixel food add score, jump and increase snake size
    if snake.head.distance(food) < 17:
        food.reposition()
        snake.extend_snake()
        scoreboard.add_score()

    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 260 or snake.head.ycor() < -290:
        game_Is_Running = False
        scoreboard.game_over()

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_Is_Running = False
            scoreboard.game_over()

screen.exitonclick()
