# Write a program to demonstrate the use of a class variable in Python by storing and displaying the bank’s interest rate.

# Description
# Create a Bank class with a class variable interest_rate.
# Create multiple objects of the Bank class.
# Print the interest rate for each object.
# Show that the class variable is shared across all objects

class Bank:
    interest_rate = 6.5

bank1 = Bank()
bank2 = Bank()

print(bank1.interest_rate)
print(bank2.interest_rate)
