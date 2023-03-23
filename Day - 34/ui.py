from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():


    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.score = 0
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)



        self.score_label = Label(text=f"Score: {self.quiz.score}",bg=THEME_COLOR,fg='white',pady=20,padx=20).grid(row=0,column=1)


        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0,)
        self.question_text = self.canvas.create_text(150, 125, text="Title",width=280, fill=THEME_COLOR, font=('Arial 12 italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=40)





        yes_button_image = PhotoImage(file='images/true.png')
        self.button_yes = Button(width=100, height=97,bg='white', image=yes_button_image, highlightthickness=0,borderwidth=0, command=self.is_known,pady=20,padx=20).grid(row=2, column=0)




        no_button_image = PhotoImage(file='images/false.png')
        self.button_yes = Button(width=100, height=97,bg='white', image=no_button_image, highlightthickness=0,borderwidth=0, command=self.is_not_known,pady=20,padx=20).grid(row=2, column=1)


        self.new_question()


        # self.ubdate_score()
        self.window.mainloop()

    def is_known(self):  # True

        if self.quiz.check_answer(user_answer='True'):
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')

        self.window.after(1000,self.new_question())


    def is_not_known(self):  # False
        if self.quiz.check_answer(user_answer='False'):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000,self.new_question())





    # def ubdate_score(self):
    #     self.score_label.itemconfig(text=self.quiz.return_score())


    def new_question(self):
        self.canvas.config(bg='white')


        try:
            question = self.quiz.next_question().split('(')
            self.canvas.itemconfig(self.question_text, text=question[0])
        except IndexError:
            self.canvas.itemconfig(self.question_text, text='Your Answered all the questions ')



