class User:
    def __init__(self, myName, myEmail, myBalance):
        self.name = myName
        self.email = myEmail
        self.accountBalance = myBalance

    def make_withdrawal(self, myAmount):
        self.accountBalance -= myAmount

    def display_user_balance(self):
        print("User:",self.name, "Balance:", self.accountBalance)

    def make_deposit(self, myAmount):
        self.accountBalance += myAmount

    def transfer_money(self, other_user, myAmount):
        self.make_withdrawal(myAmount)
        other_user.make_deposit(myAmount)


reina = User("Reina", "reina@gmail.com", 0)
mohammad = User("Mohammad", "mohammad@gmail.com", 0)
saad = User("Saad", "saad@gmail.com", 0)

reina.make_deposit(400)
reina.make_deposit(100)
reina.make_deposit(45)
reina.make_withdrawal(200)
reina.display_user_balance()

mohammad.make_deposit(1500)
mohammad.make_deposit(10)
mohammad.make_withdrawal(600)
mohammad.make_withdrawal(200)
mohammad.display_user_balance()

saad.make_deposit(1000)
saad.make_withdrawal(200)
saad.make_withdrawal(200)
saad.make_withdrawal(200)
saad.display_user_balance()

reina.transfer_money(saad, 20)
reina.display_user_balance()
saad.display_user_balance()