
from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALLIGMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", 'r') as file:
            highscore = file.read()
            self.highscore = int(highscore)

        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.color('white')
        self.write(f'Your Score: {self.score} Hight score {self.highscore}', align=ALLIGMENT, font=FONT)
        self.penup()


    def ubdate_scoreboard(self):
        self.clear()
        self.write(f'Your Score: {self.score} Hight score {self.highscore}', align=ALLIGMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.ubdate_scoreboard()

    def reset(self):

        if self.score > self.highscore:
            file = open('data.txt', 'w')
            print(self.score)
            file.write(str(self.score))
            file.close()


        self.score = 0
        self.ubdate_scoreboard()




    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'GAME OVER', align=ALLIGMENT, font=FONT)

