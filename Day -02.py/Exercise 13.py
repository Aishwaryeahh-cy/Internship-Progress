# ---------------- TRANSACTION CLASS ----------------

class Transaction:

    def __init__(self, transaction_type, amount):

        self.transaction_type = transaction_type
        self.amount = amount


    def display(self):

        print(
            self.transaction_type,
            ": ₹",
            self.amount
        )



# ---------------- ACCOUNT CLASS ----------------

class Account:


    def __init__(self, account_no, holder_name):

        self.account_no = account_no
        self.holder_name = holder_name

        # Encapsulation
        self.__balance = 0

        # Transaction history
        self.transactions = []



    def deposit(self, amount):

        self.__balance += amount


        transaction = Transaction(
            "Deposit",
            amount
        )


        self.transactions.append(transaction)


        print(
            "Amount deposited successfully"
        )



    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount


            transaction = Transaction(
                "Withdraw",
                amount
            )


            self.transactions.append(transaction)


            print(
                "Amount withdrawn successfully"
            )

        else:

            print(
                "Insufficient balance"
            )



    def get_balance(self):

        return self.__balance



    def transfer(self, account, amount):

        if amount <= self.__balance:


            self.__balance -= amount


            account.__balance += amount


            self.transactions.append(
                Transaction(
                    "Transfer Sent",
                    amount
                )
            )


            account.transactions.append(
                Transaction(
                    "Transfer Received",
                    amount
                )
            )


            print(
                "Transfer successful"
            )


        else:

            print(
                "Transfer failed"
            )



    def mini_statement(self):

        print("\n------ MINI STATEMENT ------")


        for transaction in self.transactions:

            transaction.display()


        print(
            "Current Balance: ₹",
            self.__balance
        )



    # Parent method
    def calculate_interest(self):

        return 0



# ---------------- SAVINGS ACCOUNT ----------------

class SavingsAccount(Account):


    def __init__(self, account_no, holder_name):

        super().__init__(
            account_no,
            holder_name
        )


    # Method overriding
    def calculate_interest(self):

        interest_rate = 5


        interest = (
            self.get_balance()
            * interest_rate
            / 100
        )


        return interest



# ---------------- CURRENT ACCOUNT ----------------

class CurrentAccount(Account):


    def __init__(
        self,
        account_no,
        holder_name
    ):

        super().__init__(
            account_no,
            holder_name
        )


        self.overdraft_limit = 10000



    # Method overriding
    def withdraw(self, amount):

        if amount <= (
            self.get_balance()
            +
            self.overdraft_limit
        ):


            # Access parent deposit/withdraw logic
            current_balance = self.get_balance()


            transaction = Transaction(
                "Withdraw",
                amount
            )


            self.transactions.append(
                transaction
            )


            print(
                "Amount withdrawn using overdraft"
            )


        else:

            print(
                "Overdraft limit exceeded"
            )



# ---------------- BANK CLASS ----------------

class Bank:


    def __init__(self, name):

        self.name = name

        self.accounts = []



    def create_account(self, account):

        self.accounts.append(account)


        print(
            "Account created successfully"
        )



    def show_accounts(self):

        for account in self.accounts:

            print(
                account.account_no,
                account.holder_name
            )



# ---------------- MAIN PROGRAM ----------------


bank = Bank(
    "ABC Bank"
)



# Create Accounts

savings = SavingsAccount(
    101,
    "Anusha"
)


current = CurrentAccount(
    102,
    "Rahul"
)



# Add accounts to bank

bank.create_account(
    savings
)


bank.create_account(
    current
)



# Deposit money

savings.deposit(50000)

current.deposit(20000)



# Withdraw

savings.withdraw(5000)


current.withdraw(25000)



# Transfer money

savings.transfer(
    current,
    10000
)



# Mini Statement

savings.mini_statement()


current.mini_statement()



# Interest calculation

print(
    "Savings Interest:",
    savings.calculate_interest()
)


print(
    "Current Interest:",
    current.calculate_interest()
)