from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = "✓"
reps = 0
display = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    global display
    window.after_cancel(timer)

    title_label.config(text='Timer')
    display = ""
    reps = 0
    check_lebel.config(text=display, fg=PINK)
    canvas.itemconfig(timer_text, text='00:00')



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    global display

    work_seconds = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60




    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Long Break',fg=RED)

        check_lebel.config(text=' ',fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Short Break',fg=PINK)
        display = display + check_mark
        check_lebel.config(text=display,fg=PINK)

    else:
        count_down(work_seconds)
        title_label.config(text='Work',fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_minute = int(count / 60)
    count_second = count % 60

    if count_second <10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_second }")
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()








# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomadoro App')
window.config(padx=100,pady=50,bg=YELLOW)



#Title

title_label = Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,'bold'))
title_label.grid(row=0,column=1)

#Canval
canvas = Canvas(width=200,height=233,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100,120,image=tomato_image)

timer_text = canvas.create_text(100,135,text='00:00',fill='white',font=(FONT_NAME,30,'bold'))


canvas.grid(row=1,column=1)

check_lebel = Label(text="", bg=YELLOW, fg=RED, font=(FONT_NAME, 20, 'bold'))
check_lebel.grid(row=3, column=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2,column=0)


reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=2,column=2)

#check mark lavel





















window.mainloop()