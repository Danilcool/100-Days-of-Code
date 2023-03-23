from turtle import Turtle, Screen


timmy_the_turtle = Turtle()

timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('bisque3')
timmy_the_turtle.speed(0)

moving = True
moving_value = 360
starting_angles = 3
while starting_angles != 11:
    for number in range(starting_angles):
        timmy_the_turtle.forward(90)
        timmy_the_turtle.right( moving_value / starting_angles)
        print(moving_value/starting_angles)
    starting_angles += 1




screen = Screen()
screen.exitonclick()
