from Errors import NegativeAmountError, InsufficientFundsError
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        try: #This kinda feels dirty, is there a better way to do this? 
            if amount <0: #Like, trying and failing to raise an exception feels like a super weird thing to be standard
                raise NegativeAmountError(amount) #If it works it works i guess ‾\(-_-)/‾
        except NegativeAmountError:
            print("Unable to perform transaction, you must enter a positive value")
        else:
            self.balance += amount


    def withdraw(self, amount):
        try:
            if amount<0:
                raise NegativeAmountError(amount)
            elif (self.balance-amount) < 0:
                raise InsufficientFundsError(self.balance)
            else:
                self.balance -= amount
        except NegativeAmountError:
            print("Unable to perform transaction, you must enter a positive value")
        except InsufficientFundsError:
            print("Unable to perform transaction: Insufficient funds for withdrawal")

    def get_balance(self):
        return self.balance