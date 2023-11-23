from tkinter import *
import Bank
import Account

def register_user():
    print("user registered")
    
def register():
    win1 = Toplevel()
    win1.title("Register")
    win1.geometry("350x300")

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
    register_button = Button(win1, text="Register",)
    register_button.pack()
    
    win1.mainloop()



win = Tk()
win.title(' JOJO BANKING')
win.geometry( "350x300")
Title_Lable = Label(text= "Welcome to JOJO Banking", font= ("Calibri, 13"))
Title_Lable.pack()
Label(text= "").pack()
Login_Button = Button(text= "Login", height= "2", width= "25")
Login_Button.pack()
Label(text= "").pack()
Register_Button = Button(text= "Register", height= "2", width= "25", command= register)
Register_Button.pack()



win.mainloop()
