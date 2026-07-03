# Write a program to demonstrate inheritance using a parent and child class to validate a bank account balance.

# Description
# Create a parent class BankAccount with a balance attribute.
# Create a child class that inherits from the BankAccount class.
# Use the super() method to pass the balance value to the parent class constructor.
# Based on the balance amount, display the balance status.

# Balance Conditions
# If balance is 500 or more, print “Sufficient Balance”
# If balance is less than 500, print “Low Balance”

class BankAccount:
    def __init__(self, balance):
        self.balance= balance

class SavingAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def check_balance(self):
        if self.balance >= 500:
            return 'Sufficient Balance'

        else:
            return 'Low Balance'

s= SavingAccount(float(input()))
print(s.check_balance())
