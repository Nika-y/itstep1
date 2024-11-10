class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

class Bank:
    def deposit(self, account, amount):
        account.balance += amount

    def withdraw(self, account, amount):
        if amount <= account.balance:
            account.balance -= amount

    def transfer(self, from_account, to_account, amount):
        if amount <= from_account.balance:
            from_account.balance -= amount
            to_account.balance += amount
acc1 = BankAccount("Назар", "123", 1000)
acc2 = BankAccount("Кіра", "456", 500)

bank = Bank()
bank.deposit(acc1, 200)
bank.withdraw(acc1, 100)
bank.transfer(acc1, acc2, 300)

print(acc1.balance)
print(acc2.balance)
