import string
from tkinter import *
from tkinter import ttk

root = Tk()

username = StringVar()
password = StringVar()
new_username = StringVar()
new_password = StringVar()

def check(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            #List of words (without punctuation)
            words = [word.strip(string.punctuation) for word in line.split()]
            if string_to_search in words:
                return True
    return False

def enter1():
    correct = check("Users.txt", username.get() + password.get())
    if correct == True:
       for widgets in root.winfo_children():
            widgets.destroy()
            login_message = Label(root,  text="Succesfull login.").grid(row=0, column=0)   
            secret_messge = Label(root,  text="TEXT GOES HERE").grid(row=1, column=0)   
    else:
        mylabel = Label(root, text="incorect login, FOOL!").grid(row=2, column=0)
        
    username_enter.delete(0, 'end')
    password_enter.delete(0, 'end')

def enter2():
    f = open("Users.txt", "w")
    f.write(new_username.get() + new_password.get())
    new_username_enter.delete(0, 'end')
    new_password_enter.delete(0, 'end')

username_text = Label(root, text="Please enter your username: ")
password_text = Label(root, text="Please enter your password: ")
username_enter = Entry(root, textvariable=username)
password_enter = Entry(root, textvariable=password)
enter_buttton1 = Button(root, text="Enter", width=10, command=enter1)

new_username_text = Label(root, text="Please enter a username: ")
new_password_text = Label(root, text="Please enter a password: ")
new_username_enter = Entry(root, textvariable=new_username)
new_password_enter = Entry(root, textvariable=new_password)
enter_buttton2 = Button(root, text="Enter", width=10, command=enter2)

username_text.grid(row=0, column=0)
password_text.grid(row=1, column=0)
username_enter.grid(row=0, column=1)
password_enter.grid(row=1, column=1)
enter_buttton1.grid(row=2, column=1)

new_username_text.grid(row=3, column=0)
new_password_text.grid(row=4, column=0)
new_username_enter.grid(row=3, column=1)
new_password_enter.grid(row=4, column=1)
enter_buttton2.grid(row=5, column=1)

root.mainloop()