#BellP6 Supplemental
#Purpose: To Demonstrate proficiency in error handling
class NegativeAmountError(Exception): #name and subclass
    def __init__(self, amount, message="Negative values are unacceptable"):
        self.amount = amount
        self.message = message
        super().__init__(f"{message}, you entered: {amount}") #Gibbit to the superclass, we're gonna need it there
    def __str__(self):
        return f"{self.message}, you entered: {self.amount}" #Gibbit to whoever asks for it
    
    ##Do it all again
class InsufficientFundsError(Exception):
    def __init__(self, balance, message="Unable to perform transaction: Insufficient Funds"):
        self.balance = balance
        self.message = message
        super().__init__(f"{message}, current balance: {balance}")
    def __str__(self):
        return f"{self.message}, current balance: {self.balance}"
class AccountNotExist(Exception):
    def __init__(self, account):
        pass