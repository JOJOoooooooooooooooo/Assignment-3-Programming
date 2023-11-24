from tkinter import *


def savings():
    win7 = Toplevel(win)
    win3.destroy()
    win7.title(a1.Account_Holder_Name + "'s Savings Account")
    win7.geometry("350x300")
    username_savings = Label(win7, text= a1.Account_Holder_Name + "'s Savings Account", font= ("Calibri, 13"))
    username_savings.pack()

    number_savings = Label(win7, text= "Account Number: #" + str(a1.Account_Number), font= ("Calibri, 13"))
    number_savings.pack()


    savings_amount = Label(win7, text= a2.Current_Balance, font=("Calibri, 13"))
    savings_amount.pack()
    savings_depositlabel = Label(win7, text= "deposit: ")
    savings_depositlabel.pack()
    savings_depositinput = Entry(win7)
    savings_depositinput.pack()
    def triggerdeposit():
        amount = float(savings_depositinput.get())
        print(a2.deposit(amount))
        win7.destroy()
        savings()
        
    deposit_button = Button(win7, text= "Deposit", command= triggerdeposit)
    deposit_button.pack()

    savings_withdrawlabel = Label(win7, text= "withdraw: ")
    savings_withdrawlabel.pack()

    savings_withdrawinput = Entry(win7)
    savings_withdrawinput.pack()   

    def triggerwithdraw():
        amount = float(savings_withdrawinput.get())
        withdrawstring=(a2.withdraw(amount))
        if withdrawstring == "Cannot go below $5000.0" or withdrawstring == "Value withdrawn must be postive number":
            win8 = Toplevel(win)
            win8.title("Error")
            win8.geometry("400x150")
            Label(win8, text= withdrawstring, font= ("Calibri, 13")).pack()
            Button(win8, text= "OK", command= win8.destroy).pack()
        
        win7.destroy()
        savings()
        
    withdraw_button = Button(win7, text= "Withdraw", command= triggerwithdraw)
    withdraw_button.pack()
    Button(win7, text= "Back", command= login_session).pack()

def chequing():
    win6 = Toplevel(win)
    win3.destroy()
    win6.title(a1.Account_Holder_Name + "'s Chequing Account")
    win6.geometry("350x300")
    username_chequing = Label(win6, text= a1.Account_Holder_Name + "'s Chequing Account", font= ("Calibri, 13"))
    username_chequing.pack()

    number_chequing = Label(win6, text= "Account Number: #" + str(a1.Account_Number), font= ("Calibri, 13"))
    number_chequing.pack()

    chequing_amount = Label(win6, text= a3.Current_Balance, font=("Calibri, 13"))
    chequing_amount.pack()
    chequing_updraft = Label(win6, text= "Updraft Limit: -5000.0", font=("Calibri, 10"))
    chequing_updraft.pack()
    chequing_depositlabel = Label(win6, text= "deposit: ")
    chequing_depositlabel.pack()
    chequing_depositinput = Entry(win6)
    chequing_depositinput.pack()
    def triggerdeposit():
        amount = float(chequing_depositinput.get())
        depositstring = (a3.deposit(amount))
        if depositstring == "Deposit Must be Greater Than $0":
            win10 = Toplevel(win)
            win10.title("Error")
            win10.geometry("400x150")
            Label(win10, text= depositstring, font= ("Calibri, 13")).pack()
            Button(win10, text= "OK", command= win10.destroy).pack()
        win6.destroy()
        chequing()
       
        
    deposit_button = Button(win6, text= "Deposit", command= triggerdeposit)
    deposit_button.pack()

    chequing_withdrawlabel = Label(win6, text= "withdraw: ")
    chequing_withdrawlabel.pack()

    chequing_withdrawinput = Entry(win6)
    chequing_withdrawinput.pack()   

    def triggerwithdraw():
        amount = float(chequing_withdrawinput.get())
        withdrawstring=(a3.withdraw(amount))
        print(withdrawstring)
        if withdrawstring == "Cannot go below -$5000.0" or withdrawstring == "Value withdrawn must be postive number":
            win9 = Toplevel(win)
            win9.title("Error")
            win9.geometry("400x150")
            Label(win9, text= withdrawstring, font= ("Calibri, 13")).pack()
            Button(win9, text= "OK", command= win9.destroy).pack()
        
        win6.destroy()
        chequing()
        
    withdraw_button = Button(win6, text= "Withdraw", command= triggerwithdraw)
    withdraw_button.pack()
    Button(win6, text= "Back", command= login_session).pack()

def login_session():
    global win3
    win2.destroy()
    win3 = Toplevel()
    win3.title(username1 + "'s Banking")
    win3.geometry("350x300")
    usernamebanking_label = Label(win3, text= username1 + "'s Banking", font= ("Calibri, 15"))
    usernamebanking_label.pack()

    numberbanking_label = Label(win3, text= "Account Number: #" + str(a1.Account_Number), font= ("Calibri, 13"))
    numberbanking_label.pack()

    interestrate_label = Label(win3, text= "Interest Rate: 5.25%", font= ("Calibri, 13"))
    interestrate_label.pack()

    Chequing_Button = Button(win3, text= "Checking", command= chequing)
    Savings_Button = Button(win3, text= "Savings", command= savings)
    Savings_Button.pack()
    Chequing_Button.pack()

    

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
            login_session()
            a1.set_account_holder_name(username1)
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

    

