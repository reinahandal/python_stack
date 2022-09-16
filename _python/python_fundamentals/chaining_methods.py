class User:
    def __init__(self, myName, myEmail, myBalance):
        self.name = myName
        self.email = myEmail
        self.accountBalance = myBalance

    def make_withdrawal(self, myAmount):
        self.accountBalance -= myAmount
        return self

    def display_user_balance(self):
        print("User:",self.name, "Balance:", self.accountBalance)
        return self

    def make_deposit(self, myAmount):
        self.accountBalance += myAmount
        return self

    def transfer_money(self, other_user, myAmount):
        self.make_withdrawal(myAmount)
        other_user.make_deposit(myAmount)
        return self


reina = User("Reina", "reina@gmail.com", 0)
mohammad = User("Mohammad", "mohammad@gmail.com", 0)
saad = User("Saad", "saad@gmail.com", 0)

reina.make_deposit(400).make_deposit(100).make_deposit(45).make_withdrawal(200).display_user_balance()

mohammad.make_deposit(1500).make_deposit(10).make_withdrawal(600).make_withdrawal(200).display_user_balance()

saad.make_deposit(1000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).display_user_balance()

reina.transfer_money(saad, 20).display_user_balance()
saad.display_user_balance()