from turtle import Turtle


class Snake:
    def __init__(self):
        self.cord = [(-40, 0), (-20, 0), (0, 0)]
        self.snake_body = []
        for index, piece_cord in enumerate(self.cord):
            self.snake_body.append(Turtle())
            self.snake_body[index].penup()
            self.snake_body[index].color("white")
            self.snake_body[index].shape("square")
            self.snake_body[index].setpos(piece_cord)
        self.snake_body[len(self.snake_body) - 1].color("blue")
        self.head_cord_x = round(self.snake_body[len(self.snake_body) - 1].position()[0])
        self.head_cord_y = round(self.snake_body[len(self.snake_body) - 1].position()[1])
        self.last_tail = self.snake_body[0].position()
        self.game_on = True
    def move(self):
        for index in range(0, len(self.snake_body) - 1):
            self.snake_body[index].setpos(self.snake_body[index + 1].pos())
            self.cord[index] = self.snake_body[index + 1].pos()
        self.snake_body[len(self.snake_body) - 1].forward(20)
        self.head_cord_x = round(self.snake_body[len(self.snake_body) - 1].position()[0])
        self.head_cord_y = round(self.snake_body[len(self.snake_body) - 1].position()[1])

        self.last_tail = self.snake_body[0].position()
        self.cord[0] = self.snake_body[len(self.snake_body) - 2].pos()

    def game_over_check(self, screen):
        self.head_cord_x = round(self.snake_body[len(self.snake_body) - 1].position()[0])
        self.head_cord_y = round(self.snake_body[len(self.snake_body) - 1].position()[1])
        self.wind_frame = screen.window_width() / 2
        if abs(self.head_cord_x) >= self.wind_frame or abs(self.head_cord_y) >= self.wind_frame:
            print("game over")
            self.game_on = False
        else:
            for index in range(len(self.snake_body) - 2):
                if self.head_cord_x == round(self.snake_body[index].pos()[0]) and self.head_cord_y == round(self.snake_body[index].pos()[1]):
                    print("game over")
                    self.game_on = False
                else:
                    self.game_on = True

    def right(self):
        self.snake_body[len(self.snake_body) - 1].right(90)

    def left(self):
        self.snake_body[len(self.snake_body) - 1].left(90)

    def eat(self):
        self.snake_body.insert(0, Turtle())
        self.cord.insert(0, self.last_tail)
        self.snake_body[0].penup()
        self.snake_body[0].color("white")
        self.snake_body[0].shape("square")
        self.snake_body[0].setpos(self.last_tail)
