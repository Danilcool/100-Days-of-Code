import turtle
from turtle import Turtle, Screen

import turtle as t
import random

turtle.colormode(255)

tim = t.Turtle()
turtle_moving = True
tim.speed(0)
tim.pensize(9)
########### Challenge 4 - Random Walk ########
def random_colour():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r,g,b)
possible_moves = [90,180,270,360]
while turtle_moving:
    tim.pencolor(random_colour())
    tim.forward(30)
    tim.right(random.choice(possible_moves))




screen = Screen()
screen.exitonclick()
