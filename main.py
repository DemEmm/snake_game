import random
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from Score_board import ScoreBoard
import time
import sys


# def game_end():
#     text_board.text_screen.clear()
#     text_board.text_screen.write(
#         f'''Game over, your final Score is: {text_board.Score}\nPress any key to start a new game...''',
#         False, "center", font=text_board.style)
#     my_screen.onkey(fun=new_game, key="")
#
# def new_game():
#     my_screen.onkey(fun=None, key="")
#     create_arrow()
#     my_screen.onkey(fun=do, key="r")
#     text_board.text_screen.clear()
#     text_board.text_screen.write(f''':New Game\n:Close snake game''', False, "center", font=text_board.style)
#
#     my_screen.onkey(fun=up, key="Up")
#     my_screen.onkey(fun=down, key="Down")
#
# def create_arrow():
#     arrow.color("white")
#     arrow.setpos(-105, 261)
#     arrow.showturtle()
#     my_screen.update()


def do():
    if arrow.pos()[1] == 285:
        print("up")
        snake.game_on = False
    elif arrow.pos()[1] == 261:
        print("down")
        snake.game_on = False


def up():
    text_board.text_screen.clear()
    text_board.text_screen.write(f''':New Game\n:Close snake game''', False, "center", font=text_board.style)
    arrow.setposition(-105, 285)
    my_screen.update()


def down():
    text_board.text_screen.clear()
    text_board.text_screen.write(f''':New Game\n:Close snake game''', False, "center", font=text_board.style)
    arrow.setposition(-105, 261)
    my_screen.update()


my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
my_screen.listen()

food = Food(my_screen)

snake = Snake()
snake_body = snake.snake_body
snake.game_on = True
text_board = ScoreBoard(my_screen, snake)

arrow = Turtle()
arrow.penup()
arrow.hideturtle()

while snake.game_on:

    my_screen.update()
    snake.move()

    if snake.head_cord_x == food.cord_x and snake.head_cord_y == food.cord_y:
        snake.eat()
        food.new_food()

        text_board.score_up()

    my_screen.onkey(snake.right, 'd')
    my_screen.onkey(snake.left, 'a')

    time.sleep(0.1)
    snake.game_over_check(my_screen)
    # if snake.game_on == False:
    #     game_end()
    # print("test")


# my_screen.mainloop()
