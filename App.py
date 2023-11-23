from tkinter import *
import Bank
import Account
import os

def register_user():
    username_info = username.get()
    password_info = password.get()

    #creating text file in folder with username and password
    file=open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_input.delete(0, END)
    password_input.delete(0, END)

    Regiser_label = Label(win1, text= "Account has been Created", fg = "green")
    Regiser_label.pack()

    print("user registered")#just to make sure its working correctly

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            print("Login Success")
        else:
            print("Incorrect Password")
    else:
        print("Username not found")



def register():
    global win1
    win1 = Toplevel(win)
    win1.title("Register")
    win1.geometry("350x300")

    global username
    global password
    global username_input
    global password_input
    username = StringVar()
    password = StringVar()

    Label(win1, text= "Please Create an Account").pack()
    Label(win1, text= "").pack()
    username_label = Label(win1, text= "Username ")
    username_label.pack()
    username_input = Entry(win1, textvariable= username)
    username_input.pack()
    password_label = Label(win1, text= "Password ")
    password_label.pack()
    password_input = Entry(win1, textvariable= password)
    password_input.pack()
    Label(win1, text= "").pack()
    register_button = Button(win1, text="Register", command= register_user)
    register_button.pack()
    
    win1.mainloop()



def login():
    global win2
    win2 = Toplevel (win)
    win2.title("Login")
    win2.geometry("350x300")
    login_details = Label(win2, text= "Please Log in")
    login_details.pack()
    Label(win2, text= "").pack()

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify = StringVar()
    password_verify = StringVar()

    login_username = Label(win2, text= "Username")
    login_username.pack()
    username_entry1 = Entry(win2, textvariable= username_verify)
    username_entry1.pack()

    Label(win2, text= "").pack()
    login_password = Label(win2, text= "Password")
    login_password.pack()
    password_entry1 = Entry(win2, textvariable= password_verify)
    password_entry1.pack()
    Label(win2, text= "").pack()
    Login_Button = Button(win2, text= "Login", width= 10, height = 1, command= login_verify)
    Login_Button.pack()

    win2.mainloop()

    



win = Tk()
win.title(' JOJO BANKING')
win.geometry( "350x300")
Title_Lable = Label(text= "Welcome to JOJO Banking", font= ("Calibri, 13"))
Title_Lable.pack()
Label(text= "").pack()
Login_Button = Button(text= "Login", height= "2", width= "25", command= login)
Login_Button.pack()
Label(text= "").pack()
Register_Button = Button(text= "Register", height= "2", width= "25", command= register)
Register_Button.pack()



win.mainloop()
