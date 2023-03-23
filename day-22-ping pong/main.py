from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.screensize(800,600)
screen.bgcolor('black')
screen.tracer(0)


screen.listen()

r_paddle = Paddle((410,0))
l_paddle = Paddle((-410,0))

screen.onkey(r_paddle.go_up,'w')
screen.onkey(r_paddle.go_down,'s')

screen.onkey(l_paddle.go_up,'Up')
screen.onkey(l_paddle.go_down,'Down')

ball = Ball()

scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.color('white')
scoreboard.shapesize(12)
scoreboard.goto(0,380)



while l_paddle.score != 3 and r_paddle.score != 3:
    scoreboard.clear()
    scoreboard.write(f'{r_paddle.score} : {l_paddle.score}')
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 382 or ball.ycor() < -382:
        ball.bounce()

    # detect the ball colission with apdle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 390 or ball.distance(l_paddle) < 50 and ball.ycor() > -390 :
        ball.bounce_x()
        ball.speed_up()

    if ball.xcor() > 450:
        r_paddle.score_up()

        ball.reset()

    if ball.xcor() < -450:
        l_paddle.score_up()

        ball.reset()




screen.exitonclick()