# Create base class Account with method get_balance(). 
# Create child class SavingsAccount with method calculate_interest(). 
# Create another child class FinalAmount that adds interest only if balance is greater than 1000.

class Account:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def calculate_interest(self):
        return self.get_balance() * 5 / 100


class FinalAmount(SavingsAccount):
    def get_final_amount(self):
        balance = self.get_balance()

        if balance > 1000:
            interest = self.calculate_interest()
            return balance + interest

        return balance


balance = float(input())

account = FinalAmount(balance)

print(account.get_final_amount())
