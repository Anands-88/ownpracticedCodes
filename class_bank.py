class Bank_account:

    def __init__(self,name, money):
        self.name = name
        self.money = money
    
    def deposits(self,d_amount):
        self.money += d_amount

    def withdraw(self, w_amount):
        self.money -= w_amount

    def show_balance(self):
        print("Current balance is: ",self.money)

my_account = Bank_account(input('Enter your name: '), int(input('initial deposited amount: ')))
my_account.deposits(int(input('Deposited amount: ')))
my_account.withdraw(int(input('Withdrawed amount: ')))
my_account.show_balance()