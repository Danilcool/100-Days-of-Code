from tkinter import *
import pandas
from pandas import *
import random



BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
window = Tk()
window.title('Learn Lan Game')
window.config(padx=100,pady=50,bg=BACKGROUND_COLOR)
current_card = {}


def flip_card():
    canvas_front_card.itemconfig(title_card, text='English',fill="White")
    canvas_front_card.itemconfig(word_card,text=current_card["English"],fill="White")
    canvas_front_card.itemconfig(card_image,image=back_card_image)


flip_timer = window.after(3000,func=flip_card)

#pandas set up
try:
    french_words = pandas.read_csv("data/Learned Words.csv")
except FileNotFoundError and pandas.errors.EmptyDataError:
    french_words = pandas.read_csv("data/french_words.csv")

to_learn = french_words.to_dict(orient="records")


""" Comment"""








#front card set up
canvas_front_card = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
font_card_image = PhotoImage(file='images/card_front.png')
back_card_image = PhotoImage(file='images/card_back.png')

card_image = canvas_front_card.create_image(400,263,image=font_card_image)
canvas_front_card.grid(row=0,column=1)

#labels - there 2 labels

title_card = canvas_front_card.create_text(400, 160, text="Title", fill="Black", font=('Helvetica 30 bold'))

word_card = canvas_front_card.create_text(400, 280, text="Word", fill="Black", font=('Helvetica 50 bold'))



# Yes and no set up
#yes Canvas
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas_front_card.itemconfig(title_card, text='French',fill="Black")
    final_card = canvas_front_card.itemconfig(word_card,text=current_card["French"],fill="Black")
    canvas_front_card.itemconfig(card_image, image=font_card_image,)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    #remove the card from the list to learn
    to_learn.remove(current_card)
    new_list_leanred_words = pandas.DataFrame(to_learn)
    new_list_leanred_words.to_csv("data/Learned Words.csv",mode='w',index=False)
    next_card()



yes_button_image = PhotoImage(file='images/right.png')
yes_button = Button(width=100,height=100,bg=BACKGROUND_COLOR,image=yes_button_image,highlightthickness=0,borderwidth=0,command=is_known)
yes_button.grid(row=1,column=2)

#No canvas


no_button_image = PhotoImage(file='images/wrong.png')
no_button = Button(width=100,height=100,image=no_button_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card,borderwidth=0)
no_button.grid(row=1,column=0)


























next_card()
window.mainloop()