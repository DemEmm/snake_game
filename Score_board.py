from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.text_screen = Turtle()
        self.text_screen.penup()
        self.text_screen.color("white")
        self.text_screen.hideturtle()
        self.text_screen.setpos(0, 250)
        self.style = ('Courier', 15, 'italic')
        self.Score = 0
        self.text_screen.write(f"Score: {self.Score}", False, "center", font=self.style)

    def score_up(self):
        self.Score += 1
        self.text_screen.clear()
        self.text_screen.write(f"Score: {self.Score}", False, "center", font=self.style)

    def game_end(self):
        self.text_screen.clear()
        self.text_screen.write(f"Game over, your Final Score is: {self.Score}", False, "center", font=self.style)
