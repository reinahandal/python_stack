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

    def yield_interest(self):
        self.account_balance += self.account_balance * self.interest_rate
        return self


account1 = BankAccount(0.03, 250)
account2 = BankAccount(0.06, 350)

account1.deposit(200).deposit(544).deposit(1000).withdraw(266).yield_interest().display_account_info()
account2.deposit(400).deposit(600).withdraw(150).withdraw(300).withdraw(1000).withdraw(50).yield_interest().display_account_info()