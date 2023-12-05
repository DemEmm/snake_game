import random
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from Score_board import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

food = Food(my_screen)
text_board = ScoreBoard()
snake = Snake()
snake_body = snake.snake_body

while snake.game_over_check(my_screen):

    my_screen.update()
    snake.move()

    if snake.head_cord_x == food.cord_x and snake.head_cord_y == food.cord_y:
        snake.eat()
        food.new_food()

        text_board.score_up()

    my_screen.onkey(snake.right, 'd')
    my_screen.onkey(snake.left, 'a')
    my_screen.listen()
    time.sleep(0.1)

text_board.game_end()
my_screen.mainloop()
