# Write a function that reads an integer from the user and prints it inside the function.
# The variable is created locally within the function and is not accessible outside it.
# The output should display only the entered value.

def display_number():
    number = int(input())
    print(number)


display_number()
