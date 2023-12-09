import random
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from Score_board import ScoreBoard
import time
import sys

resp = True


def nothing():
    pass


def game_end():
    text_board.text_screen.clear()
    text_board.text_screen.write(
        f'''Game over, your final Score is: {text_board.Score}\nPress any key to start a new game...''',
        False, "center", font=text_board.style)
    my_screen.onkey(fun=new_game, key="")


def new_game():
    my_screen.onkey(fun=nothing, key="")
    create_arrow()

    text_board.text_screen.clear()
    text_board.text_screen.write(f''':New Game\n:Close snake game''', False, "center", font=text_board.style)

    my_screen.onkey(fun=do, key="r")
    my_screen.onkey(fun=up, key="Up")
    my_screen.onkey(fun=down, key="Down")


def create_arrow():
    arrow.color("white")
    arrow.setpos(-105, 261)
    arrow.showturtle()
    my_screen.update()


def do():
    if arrow.pos()[1] == 285:
        print("up")
        global continue_game
        continue_game = True

        snake.game_on = True
    elif arrow.pos()[1] == 261:
        print("down")
        global game_on
        game_on = False


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

text_board = ScoreBoard(my_screen, snake)

arrow = Turtle()
arrow.penup()
arrow.hideturtle()

game_on = True
continue_game = False
while game_on:
    text_board.check_wind_size()
    if snake.game_on:
        my_screen.ontimer(snake.move(), 200)

        if snake.head_cord_x == food.cord_x and snake.head_cord_y == food.cord_y:
            snake.eat()
            food.new_food()

            text_board.score_up()

        my_screen.onkey(snake.right, 'd')
        my_screen.onkey(snake.left, 'a')

        snake.game_over_check(my_screen)
        if snake.game_on == False:
            game_end()

    else:
        if continue_game:
            my_screen.onkey(fun=nothing, key="r")
            my_screen.onkey(fun=nothing, key="Up")
            my_screen.onkey(fun=nothing, key="Down")
            for cont in snake_body:
                cont.hideturtle()
            del snake
            del snake_body

            snake = Snake()
            snake_body = snake.snake_body
            continue_game = False
            text_board.Score = 0
            text_board.text_screen.clear()
            arrow.hideturtle()
            my_screen.update()

    my_screen.update()
