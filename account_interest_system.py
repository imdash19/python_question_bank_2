# Create a base class Account with method get_balance(). 
# Create child classes SavingsAccount and CurrentAccount. 
# SavingsAccount adds 5 percent interest. CurrentAccount adds no interest.

class Account:
    def get_balance(self, balance):
        self.balance = balance


class SavingsAccount(Account):
    def calculate_balance(self):
        return self.balance + (self.balance * 0.05)


class CurrentAccount(Account):
    def calculate_balance(self):
        return self.balance


account_type = input().lower()
balance = float(input())

if account_type == "savings":
    account = SavingsAccount()
else:
    account = CurrentAccount()

account.get_balance(balance)
print(account.calculate_balance())
