from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)

my_label = Label(text='Miles',font=('Arial',24))
my_label.grid(row=0,column=2)


user_input = Entry(width=20)
user_input.grid(row=0,column=1)


equal_lavel = Label(text='is Equal to',font=('Arial',24))
equal_lavel.grid(row=1,column=0)


km_label = Label(text='Km',font=('Arial',24))
km_label.grid(row=1,column=2)

fisnished_label = Label(text=0, font=('Arial', 24))
fisnished_label.grid(row=1,column=1)


def calculate():
    finsihed_number = user_input.get()

    fisnished_label.config(text=(round(int(finsihed_number) * 1.6)))
    finsihed_number = 0


button = Button(text='Calculate',command=calculate)
button.grid(column=1,row=2)



window.mainloop()