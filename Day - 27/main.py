from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=800,height=500)



#Label
my_label = Label(text='I am a Lavel One',font=('Arial',24))
my_label.grid(column=0,row=0)


#Button

user_input = Entry(width=20,)
user_input.grid(column=4,row=2)


button = Button(text='Button')
button.grid(column=1,row=1)

button = Button(text='2nd Button')
button.grid(column=3,row=0)











# Add unlimited arguments in functions
#
# def add(a,b):
#     print(a,b)
#
# def add(*args):
#     for n in args:
#         print(n)
#
#











#listening and hast ot be at the end
window.mainloop()

