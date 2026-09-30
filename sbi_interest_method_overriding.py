# Create a parent class Bank with method get_interest(). 
# Create a child class SBI that overrides get_interest() to return 6 percent interest.

class Bank:
    def get_interest(self):
        print('6%')

class SBI(Bank):
    def get_interest(self):
        print('Interest: 6%')

SBI().get_interest()
