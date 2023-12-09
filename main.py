from turtle import Screen
from Snake import Snake
from Food import Food
from Score_board import ScoreBoard


def nothing():
    pass


my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
my_screen.listen()

food = Food(my_screen)

snake = Snake(my_screen)
snake_body = snake.snake_body

text_board = ScoreBoard(my_screen, snake)

while text_board.game_on:
    text_board.check_wind_size()
    if snake.game_on:
        my_screen.ontimer(snake.move(), 150)

        if snake.head_cord_x == food.cord_x and snake.head_cord_y == food.cord_y:
            snake.eat()
            food.new_food()

            text_board.score_up()

        my_screen.onkey(snake.right, 'Right')
        my_screen.onkey(snake.left, 'Left')

        snake.game_over_check()
        if not snake.game_on:
            text_board.game_end()

    else:
        if text_board.continue_game:
            my_screen.onkey(fun=nothing, key='space')
            my_screen.onkey(fun=nothing, key="Up")
            my_screen.onkey(fun=nothing, key="Down")
            for cont in snake_body:
                cont.hideturtle()
            del snake
            del snake_body

            snake = Snake(my_screen)
            snake_body = snake.snake_body
            continue_game = False
            text_board.Score = 0
            text_board.text_screen.clear()
            text_board.arrow.hideturtle()
            my_screen.update()
            text_board.continue_game = False
            snake.game_on = True

    my_screen.update()
