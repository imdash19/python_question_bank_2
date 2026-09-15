# Write a Python program to create a class Bank with a class variable interest_rate = 5% and 
# an instance variable account_holder. Accept account holder name from user input. 
# Create an object and display account holder name along with interest rate. 
# Show that interest rate remains constant across multiple objects. 
# Demonstrate shared financial rules using class variables.

class Bank:
    interest_rate= 5
    def __init__(self, account_holder):
        self. account_holder= account_holder

b= Bank(input())
print(f'''{b.account_holder}
Interest Rate: {b.interest_rate}%''')
