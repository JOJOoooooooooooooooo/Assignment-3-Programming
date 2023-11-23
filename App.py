from tkinter import *
import Bank
import Account
import os

def savings():
    win7 = Toplevel(win)
    win7.title(username1 + "'s Savings Account")
    win7.geometry("350x300")
    username_savings = Label(win7, text= username1 + "'s Savings Account", font= ("Calibri, 13"))
    username_savings.pack()
def chequing():
    win6 = Toplevel(win)
    win6.title(username1 + "'s Chequing Account")
    win6.geometry("350x300")
    username_chequing = Label(win6, text= username1 + "'s Chequing Account", font= ("Calibri, 13"))
    username_chequing.pack()
def login_session():
    global win3
    win2.destroy()
    win3 = Toplevel()
    win3.title(username1 + "'s Banking")
    win3.geometry("350x300")
    usernamebanking_label = Label(win3, text= username1 + "'s Banking", font= ("Calibri, 13"))
    usernamebanking_label.pack()
    Chequing_Button = Button(win3, text= "Checking", command= chequing)
    Savings_Button = Button(win3, text= "Savings", command= savings)
    Savings_Button.pack()
    Chequing_Button.pack()

def login_success():
    login_session()
def password_incorrect():
    global win4
    win4 = Toplevel(win)
    win4.title("Success")
    win4.geometry("150x100")
    loginsuccess_label = Label(win4, text= "Password Incorrect")
    loginsuccess_label.pack()
    Button(win4, text="OK", command=win4.destroy).pack()
def user_not_found():
    global win5
    win5 = Toplevel(win)
    win5.title("Success")
    win5.geometry("150x100")
    loginsuccess_label = Label(win5, text= "Username Not Found")
    loginsuccess_label.pack()
    Button(win5, text="OK", command=win5.destroy).pack()
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
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_incorrect()
    else:
        user_not_found()



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
win.geometry( "650x700")
Title_Lable = Label(text= "Welcome to JOJO Banking", font= ("Calibri, 13"))
Title_Lable.pack()
Label(text= "").pack()
bank_logo = PhotoImage(file='bank_logo.png')
my_label = Label(win, image= bank_logo)
my_label.pack()
Login_Button = Button(text= "Login", height= "2", width= "25", command= login)
Login_Button.pack()
Label(text= "").pack()
Register_Button = Button(text= "Register", height= "2", width= "25", command= register)
Register_Button.pack()



win.mainloop()
