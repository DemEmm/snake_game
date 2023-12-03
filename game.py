import random
from turtle import Turtle, Screen
import time


def right():
    snake_body[len(snake_body) - 1].right(90)


def left():
    snake_body[len(snake_body) - 1].left(90)


def new_food():
    rand_pos_x = random.randrange(int(-(my_screen.window_width() / 2)), int((my_screen.window_width() / 2)), 20)
    rand_pos_y = random.randrange(int(-(my_screen.window_width() / 2)), int((my_screen.window_width() / 2)), 20)
    food.setpos((rand_pos_x, rand_pos_y))
    print("yes")


def game_over_check():
    head_cord_x = round(snake_body[len(snake_body) - 1].position()[0])
    head_cord_y = round(snake_body[len(snake_body) - 1].position()[1])
    wind_frame = my_screen.window_width() / 2
    if abs(head_cord_x) >= wind_frame or abs(head_cord_y) >= wind_frame:
        print("game over")
        return 1
    else:
        for index in range(len(snake_body) - 2):
            if head_cord_x == round(snake_body[index].pos()[0]) and head_cord_y == round(snake_body[index].pos()[1]):
                print("game over")
                return 1
        return 0



my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)


cord = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []

food = Turtle()
food.penup()
food.color("white")
food.shape("square")


text_screen =Turtle()
text_screen.penup()
text_screen.color("white")
text_screen.hideturtle()
text_screen.setpos(0,250)
style = ('Courier', 15, 'italic')
Score=0
text_screen.write(f"Score: {Score}", False,"center" ,font=style)


rand_cord_x = random.randrange(int(-(my_screen.window_width() / 2)), int((my_screen.window_width() / 2)), 20)
rand_cord_y = random.randrange(int(-(my_screen.window_width() / 2)), int((my_screen.window_width() / 2)), 20)
food.setpos((rand_cord_x, rand_cord_y))

for index, _cord in enumerate(cord):
    snake_body.append(Turtle())
    snake_body[index].penup()
    snake_body[index].color("white")
    snake_body[index].shape("square")
    snake_body[index].setpos(_cord)

snake_body[len(snake_body) - 1].speed(0)

game_over = 0
while game_over==0:
    my_screen.update()
    for index in range(0, len(snake_body) - 1):
        snake_body[index].setpos(snake_body[index + 1].pos())

    head_cord_x = round(snake_body[len(snake_body) - 1].position()[0])
    head_cord_y = round(snake_body[len(snake_body) - 1].position()[1])
    last_tail = snake_body[0].position()
    game_over = game_over_check()


    # print("food: ", food.position()[0], ", ", food.position()[1])
    # print("snake: ", round(snake_body[len(snake_body) - 1].position()[0]), ", ", round(snake_body[len(snake_body) - 1].position()[1]))

    food_cord_x = round(food.position()[0])
    food_cord_y = round(food.position()[1])

    if head_cord_x == food_cord_x and head_cord_y == food_cord_y:
        new_food()
        snake_body.insert(0, Turtle())
        snake_body[0].penup()
        snake_body[0].color("white")
        snake_body[0].shape("square")
        snake_body[0].setpos(last_tail)
        Score+=1
        text_screen.clear()
        text_screen.write(f"Score: {Score}", False, "center", font=style)

    snake_body[len(snake_body) - 1].forward(20)
    my_screen.onkey(right, 'd')
    my_screen.onkey(left, 'a')
    my_screen.listen()
    time.sleep(0.2)

text_screen.clear()
text_screen.write(f"Game over, your Final Score is: {Score}", False,"center" ,font=style)
my_screen.mainloop()