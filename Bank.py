from tkinter import *


def register():
    win1 = Toplevel()
    win1.title("Register")
    win1.geometry("350x300")

    username = StringVar()
    password = StringVar()

    username_label = Label(win1, text= "Username ")
    username_label.pack()
    username_input = Entry(win1, textvariable= username)
    username_input.pack()
    password_label = Label(win1, text= "Password ")
    password_label.pack()
    password_input = Entry(win1, textvariable= password)
    password_input.pack()

    register_button = Button(win1, text="Register",)
    register_button.pack()
    
    win1.mainloop()



#def login():