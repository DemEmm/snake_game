import turtle
import time
x = True

def doit():
    print("Key pressed!")

def stop():
    global x
    x = False
    print("End")

my_screen = turtle.Screen()



while x:
    my_screen.listen()
    my_screen.onkey(doit, 'd')  # Bind the 'doit' function to the 'd' key press event
    my_screen.onkey(stop, 's')  # Bind the 'stop' function to the 's' key press event



