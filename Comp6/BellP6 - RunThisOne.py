#BellP6
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate proficiency with exception handling, and defining custom exceptions.


#Handle Imports.
from Account import BankAccount

def main(): #enclose everything in one callable function
    account = BankAccount(100) #instantiate BankAccount as the object account
    print("Initial Balance:", account.get_balance())

    while True: #open a loop
        choice = input("Do you want to (d)eposit, (w)ithdraw, or (q)uit? ").strip().lower() #Accept interaction option for menu
        if choice == 'q':
            try:
                del account
                break
            except Exception as e:
                raise
            finally: #This is unnecessary except the Program Spec required I demonstrate I know how to use a finally statement
                #So well do some... nefarious cleanup MUAHUAHUA
                exit("Account Successfully deleted: Goodbye *\\(^⊎^)")
                
        elif choice == 'd':
            try:
                deposit_amount = float(input("Enter deposit amount: "))
                account.deposit(deposit_amount) #call the deposit method from Account.py
                print("Balance after deposit:", account.get_balance())
            except Exception as e: #raise exceptions gracefully, as defined in Errors.py
                raise
        elif choice == 'w':
            try:
                withdraw_amount = float(input("Enter withdrawal amount: "))
                account.withdraw(withdraw_amount) #call the withdraw method from Account.py
                print("Balance after withdrawal:", account.get_balance())
            except Exception as e:
                raise
        else:
            print("Invalid selection. Please choose 'd', 'w', or 'q'.") #Super basic input sanitizing
    
    print("Final Balance:", account.get_balance()) 

if __name__ == "__main__":
    main()
