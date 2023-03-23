from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for num in range(randint(8,10))]

    password_symbols = [choice(numbers) for num in range(randint(2,4))]

    password_number = [choice(numbers) for num in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_number
    shuffle(password_list)
    print(password_list)
    final_password = "".join(password_list)



    password_entry.insert(0,final_password)
    pyperclip.copy(final_password)






# ---------------------------- Search PASSWORD ------------------------------- #

def search_passoword():
    website = website_entry.get()
    try:
        with open("Saved Passwords.json") as file:
            data = json.load(file)
            password = data[website]

            messagebox.showinfo(title='Passowrd', message=f'Your password for {website} is :\n{password["password"]}')
    except KeyError or FileNotFoundError:
        messagebox.showinfo(title='Error', message=f'You have not saved passowrd for {website} yet')



# ---------------------------- UI SETUP ------------------------------- #
#image
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

#lock logo

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_image)

canvas.grid(row=0,column=1)

#labels


website_label = Label(text='Website:',font=(FONT_NAME,10,'bold'))
website_label.grid(row=1,column=0)

website_entry = Entry(width=20)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()
website_search = Button(text='Search',command=search_passoword,width=7,)
website_search.grid(row=1,column=2,columnspan=1)


email_label = Label(text='Email/Username:',font=(FONT_NAME,10,'bold'))
email_label.grid(row=2,column=0)

email_entry = Entry(width=41)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(index=0,string='danilovcharenk2@gmail.com')

password_label = Label(text='Password',font=(FONT_NAME,10,'bold'))
password_label.grid(row=3,column=0)

password_entry = Entry(width=20)
password_entry.grid(row=3,column=1)



#calls action() when pressed
button = Button(text="Generate Password", command=generate_password,width=17)
button.grid(row=3,column=2)


def add():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data  = {
        website:{
            "email": email,
            "password": password
    }}
    if website == '' or password == '':
        messagebox.showinfo(title='Warning',message='Please dont leave Website or Password empty')

    elif messagebox.askokcancel(title=website,message=f'Do you want to save:\nEmail: {email} \nPassword: {password}\n'):
        try:
            with open('Saved Passwords.json', mode='r') as file:
                data = json.load(file)
                #writing
                data.update(new_data)

        except FileNotFoundError:
            with open('Saved Passwords.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("Saved Passwords.json", mode="w") as file:
                # saving data
                json.dump(data, file, indent=4)
        finally:
                messagebox.showinfo(title='Saved', message='Your Information Has been saved')

                website_entry.delete(0, END)
                password_entry.delete(0, END)






#calls action() when pressed
button = Button(text="Add", command=add,width=35)
button.grid(row=4,column=1,columnspan=2)


#entry





















window.mainloop()