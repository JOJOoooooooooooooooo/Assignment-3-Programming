import random

class Account():
    def __init__(self, Account_Holder_Name= "Default", Current_Balance=0):
        self.Account_Number =  random.randint(1000, 10000)
        self.Account_Holder_Name = Account_Holder_Name
        self.Current_Balance = Current_Balance
        
    def set_account_number(self, number):
        self.Account_Number = number

    def set_account_holder_name(self, name):
        self.Account_Holder_Name = name

    def RateofInterest(self, CDN_Rate_of_Interest):
        self.CND_Rate_of_Interest = "5.25%"
        
    
    def deposit(self, value):
        if value > 0:
            self.Current_Balance += value
            return "Current Balance: " + str(self.Current_Balance)
        else:
            return "Deposit Must be Greater Than $0"
   
    
class SavingsAccount(Account):
    def withdraw(self, value):
        if value > 0:
            if self.Current_Balance - value < 5000.0:
                return "Cannot go below $5000.0"
            else:
                self.Current_Balance -= value
                return "Current Balance: " + str(self.Current_Balance)
        else:
            return "Value withdrawn must be postive number"
class ChequingAccount(Account):
    def withdraw(self, value):
        if value > 0:
            if self.Current_Balance - value < -5000.0:
                return "Cannot go below -$5000.0"
            else:
                self.Current_Balance -= value
                return "Current Balance: " +str(self.Current_Balance)
        else:
            return "Value withdrawn must be postive number"