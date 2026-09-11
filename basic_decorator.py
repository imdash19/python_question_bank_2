# Write a Python program to demonstrate a basic decorator.
# The decorator should print a message before and after calling the main function.
# Create a simple function greet() that prints a greeting.
# Apply the decorator to this function using @ notation.
# The program should show how decorators wrap functions.
# It should also demonstrate function calling order.
# The output should clearly show the decorator functionality.

def decorator(func):
    def wrapper():
        print('Before function call ')
        func()
        print('After function call')
    return wrapper

@decorator
def greet():
    print('Hello! Welcome to Python. ')

greet()
