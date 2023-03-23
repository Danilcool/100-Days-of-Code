from turtle import Turtle
FONT = ("Courier", 12, "normal")
ALLIGMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250,270)
        self.score = 0
        self.color('black')
        self.write(f'Level: {self.score}', align=ALLIGMENT, font=FONT)



    def score_up(self):
        self.hideturtle()
        self.score += 1
        self.clear()
        self.write(f'Level: {self.score}', align=ALLIGMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.shape('circle')
        self.hideturtle()
        self.write(f'GAME OVER', align=ALLIGMENT, font=FONT)



