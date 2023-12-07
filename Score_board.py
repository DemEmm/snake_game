from turtle import Turtle


class ScoreBoard:
    def __init__(self,screen,snake):
        self.text_screen = Turtle()
        self.text_screen.penup()
        self.text_screen.color("white")
        self.text_screen.hideturtle()
        self.text_screen.setpos(0, 250)
        self.style = ('Courier', 15, 'italic')
        self.Score = 0
        self.text_screen.write(f"Score: {self.Score}", False, "center", font=self.style)
        self.screen = screen
        self.snake = snake
    def score_up(self):
        self.Score += 1
        self.text_screen.clear()
        self.text_screen.write(f"Score: {self.Score}", False, "center", font=self.style)

    # def game_end(self):
    #     self.text_screen.clear()
    #     self.text_screen.write(
    #         f'''Game over, your final Score is: {self.Score}\nPress any key to start a new game...''',
    #         False, "center", font=self.style)
    #     self.screen.onkey(fun=self.new_game, key="")
    #
    # def new_game(self):
    #     self.screen.onkey(fun=None, key="")
    #
    #     def do():
    #         if arrow.pos()[1]==285:
    #             print("up")
    #             self.snake.game_on = False
    #         elif arrow.pos()[1]==261:
    #             print("down")
    #             self.snake.game_on = True
    #
    #     def up():
    #         self.text_screen.clear()
    #         self.text_screen.write(f''':New Game\n:Close snake game''',
    #                                False, "center", font=self.style)
    #         arrow.setposition(-105, 285)
    #         self.screen.update()
    #     def down():
    #         self.text_screen.clear()
    #         self.text_screen.write(f''':New Game\n:Close snake game''',
    #                                False, "center", font=self.style)
    #         arrow.setposition(-105, 261)
    #         self.screen.update()
    #
    #     self.screen.onkey(fun=do, key="r")
    #     self.text_screen.clear()
    #     self.text_screen.write(f''':New Game\n:Close snake game''',
    #         False, "center", font=self.style)
    #
    #     arrow = Turtle()
    #     arrow.penup()
    #     arrow.color("white")
    #     arrow.setpos(-105, 261)
    #     self.screen.update()
    #
    #     self.screen.onkey(fun=up, key="Up")
    #     self.screen.onkey(fun=down, key="Down")
    #     # self.screen.listen()
    #
    #     print("test")
        # self.text_screen.write(
        #     f'''test{self.Score}\n''',False, "center", font=self.style)
