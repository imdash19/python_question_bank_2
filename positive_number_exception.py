# Write a Python program to check if a number is positive using try-except-else blocks.Here's what you need to do:
# Take a number as input from the user.
# Use a try block to attempt converting the input to an integer.
# If the conversion fails because the user entered non-numeric input like letters or symbols, catch the ValueError exception and display an error message.
# Use an else block that executes only when the input is successfully converted to an integer without any exception.
# Inside the else block, check if the number is positive (greater than 0).
# If the number is positive, display "The number is positive".
# If the number is zero or negative, display "The number is not positive".
# The program should handle all types of inputs without crashing.
# Input Format:
# Single line contains a value which can be a number or non-numeric text.
# Output Format:
# If number > 0: Display "The number is positive".
# If number <= 0: Display "The number is not positive".
# If invalid input: Display "Error: Invalid input. Please enter a valid number".

try:
    number = int(input())

except ValueError:
    print("Error: Invalid input. Please enter a valid number")

else:
    if number > 0:
        print("The number is positive")
    else:
        print("The number is not positive")
