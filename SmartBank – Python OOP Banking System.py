class BankAccount:

    def __init__(self, name, account_no, ifsc, balance):
        self.name = name
        self.account_no = account_no
        self.ifsc = ifsc
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

    def show_details(self):
        print("\n----- Customer Details -----")
        print("Name          :", self.name)
        print("Account No    :", self.account_no)
        print("IFSC          :", self.ifsc)
        print("Balance       :", self.balance)
        print("-----------------------------")


# ------------------------------------
# Create Multiple Customers Using Input
# ------------------------------------

customers = {}

num_customers = int(input("How many customers you want to create? "))

for i in range(1, num_customers + 1):
    print(f"\nEnter details for Customer {i}:")
    name = input("Enter Name: ")
    account_no = input("Enter Account Number: ")
    ifsc = input("Enter IFSC: ")
    balance = float(input("Enter Opening Balance: "))

    customers[i] = BankAccount(name, account_no, ifsc, balance)

print("\nCustomers created successfully!")


# ------------------------------
# Menu Operations
# ------------------------------

while True:
    print("\n----- Choose an Option -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show Customer Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice in [1, 2, 3, 4]:
        cust_id = int(input("Enter Customer Number: "))

        if cust_id not in customers:
            print("Invalid customer number!")
            continue

        customer = customers[cust_id]

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        print("Updated Balance =", customer.deposit(amount))

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        print("Updated Balance =", customer.withdraw(amount))

    elif choice == 3:
        print("Balance =", customer.check_balance())

    elif choice == 4:
        customer.show_details()

    elif choice == 5:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice, try again!")
