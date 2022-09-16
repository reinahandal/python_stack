class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.interest_rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        else:
            self.account_balance -= amount
        return self

    def display_account_info(self):
        print("Balance:", self.account_balance)
        return self

class User:
    def __init__(self, myName, myEmail):
        self.name = myName
        self.email = myEmail
        self.account = BankAccount()

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("User:",self.name)
        self.account.display_account_info()
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

reina = User("Reina", "reina@handal.com")
ameer = User("Ameer", "ameer@handal.com")

reina.account.deposit(500).withdraw(200).display_account_info()