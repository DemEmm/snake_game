from turtle import Turtle
import random


class Food:
    def __init__(self, screen):
        self.food = Turtle()
        self.food.penup()
        self.food.color("white")
        self.food.shape("square")
        self.food_screen = screen
        rand_cord_x = random.randrange(int(-(screen.window_width() / 2)), int((screen.window_width() / 2)), 20)
        rand_cord_y = random.randrange(int(-(screen.window_width() / 2)), int((screen.window_width() / 2)), 20)
        self.food.setpos((rand_cord_x, rand_cord_y))

        self.cord_x = round(self.food.position()[0])
        self.cord_y = round(self.food.position()[1])

    def new_food(self):
        rand_pos_x = random.randrange(int(-(self.food_screen.window_width() / 2.5)), int((self.food_screen.window_width() / 2.5)), 20)
        rand_pos_y = random.randrange(int(-(self.food_screen.window_width() / 2.5)), int((self.food_screen.window_width() / 2.5)), 20)
        self.food.setpos((rand_pos_x, rand_pos_y))
        self.cord_x = round(self.food.position()[0])
        self.cord_y = round(self.food.position()[1])
        print("yes")
