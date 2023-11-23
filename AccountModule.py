class Account():
    def __init__(self, Account_Number, Account_Holder_Name, Current_Balance=0):
        self.Account_Number = Account_Number
        self.Account_Holder_Name = Account_Holder_Name
        self.Current_Balance = Current_Balance
        

    def RateofInterest(self):
        CND_Rate_of_Interest = 0.525
        return f'{self.Current_Balance * CND_Rate_of_Interest}' #Probably Wrong
    
    def deposit(self, value):
        if value > 0:
            self.Current_Balance += value
            return "Current Balance: " + self.Current_Balance
        else:
            return "Deposit Must be Greater Than $0"
   
    
class SavingsAccount(Account):
    def __init__(self):
        pass
    def withdraw(self, value):
        if self.Current_Balance == 5000.0:
            return "Cannot go below $5000.0"
        else:
            self.Current_Balance -= value
            return "Curremt Balance: " + self.Current_Balance

class ChequingAccount(Account):
    def __init__(self):
        pass
    def withdraw(self, value):
        if self.Current_Balance == -5000.0:
            return "Cannot go below -$5000.0"
        else:
            self.Current_Balance -= value
            return "Curremt Balance: " + self.Current_Balance