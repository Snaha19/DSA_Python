class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(self.account_holder, "balance:", self.balance)



acc1 = BankAccount("Amit", 5000)
acc2 = BankAccount("Riya", 8000)


acc1.deposit(2000)
acc1.withdraw(1500)
acc1.display_balance()


acc2.withdraw(9000)
acc2.deposit(3000)
acc2.display_balance()