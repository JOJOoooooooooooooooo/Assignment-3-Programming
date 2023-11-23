class Account():
    def __init__(self, Account_Number, Account_Holder_Name, Current_Balance, Withdraw, Deposit):
        self.Account_Number = Account_Number
        self.Account_Holder_Name = Account_Holder_Name
        self.Current_Balance = Current_Balance
        self.Withdraw = Withdraw
        self.Deposit = Deposit

    def RateofInterest(self):
        CND_Rate_of_Interest = 0.525
        return f'{self.Current_Balance} * {CND_Rate_of_Interest}'
    
class SavingsAccount(Account):
    def __init__(self):
        pass
class ChequingAccount(Account):
    def __init__(self):
        pass