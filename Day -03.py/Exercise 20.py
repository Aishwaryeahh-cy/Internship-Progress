# Bank ATM Simulation

class Account:

    # Constructor
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance


    # Deposit
    def deposit(self, amount):

        self.balance += amount

        print("Amount Deposited Successfully")


    # Withdraw
    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            print("Amount Withdrawn Successfully")

        else:

            print("Insufficient Balance")


    # Display Balance
    def display_balance(self):

        print("\nAccount Number :", self.account_number)
        print("Account Holder :", self.account_holder)
        print("Available Balance :", self.balance)



# Object

acc1 = Account(1001, "Annu", 10000)


# Menu

while True:

    print("\n------ ATM MENU ------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:

        amount = float(input("Enter Deposit Amount : "))

        acc1.deposit(amount)

    elif choice == 2:

        amount = float(input("Enter Withdrawal Amount : "))

        acc1.withdraw(amount)

    elif choice == 3:

        acc1.display_balance()

    elif choice == 4:

        print("Thank You")

        break

    else:

        print("Invalid Choice")