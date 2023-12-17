from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.food_screen = screen
        rand_cord_x = random.randrange(int(-(screen.window_width() / 2)), int((screen.window_width() / 2)), 20)
        rand_cord_y = random.randrange(int(-(screen.window_width() / 2)), int((screen.window_width() / 2)), 20)
        self.setpos((rand_cord_x, rand_cord_y))

        self.cord_x = round(self.position()[0])
        self.cord_y = round(self.position()[1])

    def new_food(self):
        board_limit_x_y = (self.food_screen.window_width()/2)-20
        rand_pos_x = random.randrange(int(-board_limit_x_y), int(board_limit_x_y), 20)
        rand_pos_y = random.randrange(int(-board_limit_x_y), int(board_limit_x_y), 20)
        self.setpos((rand_pos_x, rand_pos_y))
        self.cord_x = round(self.position()[0])
        self.cord_y = round(self.position()[1])
        print("yes")
