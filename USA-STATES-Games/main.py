import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title('USA GAME')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

writer = Turtle()
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
guessed_states = []
game_on = True

missing_states = []

while len(guessed_states) < 50:

   answer = screen.textinput(title='What is State:', prompt='whats Anouther state:').title()
   if answer == "Exit":
       for guessed_state in guessed_states:
           for state in data.state:
               if guessed_state == state:
                   pass
               else:
                   missing_states.append(state)
       new_data = pandas.DataFrame(missing_states)
       new_data.to_csv('Missing.states.csv')
       break
   for state in data.state:



       if state == answer:
         guessed_states.append(answer)

         state_info = data[data.state == answer]
         writer.penup()
         writer.color('black')
         x = state_info.x
         y = state_info.y
         writer.hideturtle()
         writer.goto(int(x), int(y))
         writer.write(answer)


print(missing_states)

turtle.mainloop()

