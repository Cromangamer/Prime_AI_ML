class BankAccount: 
    def __init__(self ,number, name, amount  ):
        self.account_number = number 
        self.holder_name = name
        self.balance = amount
        print("+_+_+_+_+_+_+_+_Account Created!+_+_+_+_+_+_+_+_")

    def deposit(self, amount):
        self.balance += amount
        print("++++++++++++++ DEPOSIT ++++++++++++++")
        print(f"Your deposit is {amount}") 
        print(f"Now you Bank balance is {self.balance}", end="\n\n")

    def withdraw(self, amount):
        self.balance -= amount
        print("++++++++++++++ Withdraw ++++++++++++++")
        print(f"Your Withdraw amount is {amount}")
        print(f"Now you Bank balance is {self.balance}", end="\n\n")

    def check_balance(self):
        print(f"Your Balance : {self.balance}")

Acc1 = BankAccount(123456789, "Dhruv", 500 )

Acc1.deposit(1000)
Acc1.withdraw(1500)
Acc1.check_balance()