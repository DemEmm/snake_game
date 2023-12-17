from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, screen, snake):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setpos(0, 250)
        self.style = ('Courier', 15, 'italic')
        self.Score = 0
        self.game_on = True
        self.continue_game = False
        self.write(f"Use arrows and space to Play\nScore: {self.Score}", False, "center", font=self.style)

        self.screen = screen
        self.snake = snake
        self.arrow = Turtle()
        self.arrow.penup()
        self.arrow.hideturtle()

    def score_up(self):
        self.Score += 1
        self.clear()
        self.write(f"Score: {self.Score}", False, "center", font=self.style)

    def check_wind_size(self):
        if self.screen.window_width() > 600 or self.screen.window_width() > 600:
            self.screen.setup(600, 600)

    def game_end(self):
        self.clear()
        self.write(
            f'''Game over, your final Score is: {self.Score}\nPress any key to start a new game...''',
            False, "center", font=self.style)
        self.screen.onkey(fun=self.new_game, key="")
        self.screen.onkey(fun=self.new_game, key="Up")
        self.screen.onkey(fun=self.new_game, key="Down")
        self.screen.onkey(fun=self.new_game, key="space")

    def new_game(self):
        self.screen.onkey(fun=None, key="")
        self.create_arrow()

        self.clear()
        self.write(f''':New Game\n:Close snake game''', False, "center", font=self.style)

        self.screen.onkey(fun=self.do, key="space")
        self.screen.onkey(fun=self.up, key="Up")
        self.screen.onkey(fun=self.down, key="Down")

    def create_arrow(self):
        self.arrow.color("white")
        self.arrow.setpos(-105, 261)
        self.arrow.showturtle()
        self.screen.update()

    def do(self):
        if self.arrow.pos()[1] == 285:
            print("up")
            self.continue_game = True

            self.snake.game_on = True
        elif self.arrow.pos()[1] == 261:
            print("down")
            self.game_on = False

    def up(self):
        self.clear()
        self.write(f''':New Game\n:Close snake game''', False, "center", font=self.style)
        self.arrow.setposition(-105, 285)
        self.screen.update()

    def down(self):
        self.clear()
        self.write(f''':New Game\n:Close snake game''', False, "center", font=self.style)
        self.arrow.setposition(-105, 261)
        self.screen.update()
