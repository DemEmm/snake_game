import random
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from Score_board import ScoreBoard
import time
import sys

text= Turtle()
text_letter = 0


def text_insert(answer):
    global text_letter
    print("hello")
    text_letter += 1

def text_lower(question,answer):
    global text_letter
    text.penup()
    text.goto(random.randint(-250,250),355)
    text.pendown()
    text.color("white")
    text.write("Start", font=("Arial", 20, "normal"))
    x,y = text.pos()
    delay = .01
    wn.textinput("Answer", "Answer:")
    turtle.listen()
    turtle.onkey(text_insert(answer),answer[text_letter])
    while y > -355:
        time.sleep(delay)
        y -= 1
        text.goto(x,y)
        text.write(question, font=("Arial", 20, "normal"))
        text.clear()