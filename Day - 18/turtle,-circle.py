import turtle
from turtle import Turtle, Screen
import random
import turtle as t
turtle.colormode(255)

tim = t.Turtle('square')
tim.speed(0)
tim.pensize(1)

def random_colour():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r,g,b)


def circle():
    radios = 360
    turn_count = 72
    while turn_count != 0:
        tim.pencolor(random_colour())
        tim.right((radios/turn_count))
        tim.circle(100)
        turn_count -= 1
circle()