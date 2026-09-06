# Read an integer as a global variable.
# Access and print the same value inside a function and again outside the function.
# The output should display the value twice, showing global accessibility.

number = int(input())

def display_number():
    print(number)

display_number()
print(number)
