# Create an Account class with a private attribute __balance.
# Use a method to display the balance in the format:
# Balance: <balance>

class Account:
    def __init__(self, balance):
        self.__balance= balance

    def display_balance(self):
        return self.__balance

a= Account(int(input()))
print(f'Balance: {a.display_balance()}')
