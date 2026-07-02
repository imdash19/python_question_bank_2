# Create a class Demo with:
# Public attribute public_data
# Private attribute __private_data
# Print both attributes:
# Public attribute can be accessed directly
# Private attribute must be accessed via a method

class Demo:
    def __init__(self, public_data, private_data):
        self.public_data= public_data
        self.__private_data= private_data

    def get_private_data(self):
        return self.__private_data

d= Demo(input(), input())

print(d.public_data, d.get_private_data())
