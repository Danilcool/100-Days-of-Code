from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,positon):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(positon)
        self.score = 0


    def go_up(self):
        y_cor = self.ycor()
        if y_cor < 350:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)


    def go_down(self):
        y_cor = self.ycor()
        if y_cor > -350:
            new_y = self.ycor() + -20
            self.goto(self.xcor(), new_y)

    def score_up(self):
        self.score += 1





