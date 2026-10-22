class Back_Account : 
    def __init__(self, account_holder_name, account_number, balance):
        self._account_holder_name = account_holder_name  # protected attribute
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


account1 = Back_Account("John Doe", "123456789", 1000)

print("Account Number: " + account1.get_account_number())  # Output: 123456789
account1.deposit(500)  # Output: Deposited: 500, New Balance: 1500
account1.withdraw(200)  # Output: Withdrew: 200, New Balance: 1300

account1.__balance = 5000  # Attempt to modify private attribute directly (will not work)
print("Balance after direct modification attempt: " + str(account1.get_balance()))  # Output: 1300