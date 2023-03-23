import turtle
from turtle import Turtle, Screen
import random
import turtle as t
import colorgram
turtle.colormode(255)
turtle = t.Turtle()
turtle.pensize(15)
turtle.penup()
colours_of_painting = colorgram.extract('dots.jpg',60)
rgb_colours = []

for color in colours_of_painting:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colours.append(new_color)
colors_full = [(194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182), (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15), (168, 208, 178), (14, 88, 104), (162, 203, 212), (220, 179, 173), (236, 204, 13),(194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182), (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15), (168, 208, 178), (14, 88, 104), (162, 203, 212), (220, 179, 173), (236, 204, 13)]
step_count = 0

def dot_move():
    turtle.color(color)
    turtle.dot()
    turtle.forward(60)
    return 1

def move_right():
    turtle.color(color)
    turtle.dot()
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)


def move_left():
    turtle.color(color)
    turtle.dot()
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)

turtle.setheading(225)
turtle.forward(400)
turtle.setheading(0)

for color in colors_full:


    step_count += dot_move()

    if step_count == 15:
        move_left()
    elif step_count == 30:
        move_right()
        step_count = 0



