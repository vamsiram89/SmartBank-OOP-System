class BankAccount:
    
    def  __init__(self,AccounName,AccountNumber,IFSC,Balance):
        
        self.AccounName    = AccounName
        self.AccountNumber = AccountNumber
        self.IFSC          = IFSC
        self.Balance       = Balance
        
        print("AccounName:    =", self.AccounName)
        print("AccountNumber: =", self.AccountNumber)
        print("IFSC:          =", self.IFSC)
        print("Balance:       =", self.Balance)

    def Deposit(self,Amount):
        self.Balance += Amount
        return self.Balance

    def withdraw(self,Amount):
        if Amount > self.Balance:
            return "Insufficient Balance"
        self.Balance -= Amount
        return self.Balance
    
    def CheckBalance(self):
        return self.Balance
        


# ------------------------------
# User Inputs to operate account
# ------------------------------
customer1 = BankAccount("vamsiram pandluru",332423484116,"SBIN0001901",10000)

while True:
    print("\n----- Choose an Option -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        print("Updated Balance =", customer1.Deposit(amount))

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        print("Updated Balance =", customer1.withdraw(amount))

    elif choice == 3:
        print("Your Balance =", customer1.CheckBalance())

    elif choice == 4:
        print("Thank you! Exiting...")
        break
    
    else:
        print("Invalid choice, try again!")
