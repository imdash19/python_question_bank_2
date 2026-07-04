# Write a program to demonstrate the use of instance variables in Python by storing and checking a bank account balance.

# Description
# Create a BankAccount class with a balance as an instance variable.
# Use the balance to decide the account status:
# If balance is 500 or more, print “Sufficient Balance”
# Otherwise, print “Low Balance

class BankAccount:
    def __init__(self, balance):
        self.balance= balance

    def check_status(self):
        if self.balance >= 500:
            return 'Sufficient Balance'

        else:
            return 'Low Balance'

b= BankAccount(float(input()))
print(b.check_status())
