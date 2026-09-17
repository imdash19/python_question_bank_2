# 1. Problem Statement Description
# Write a Python program to check voting eligibility using exception handling with try-except-else blocks.
# Here's what you need to do:

# Take the age of a person as input from the user.
# Use a try block to attempt converting the input to an integer.
# If the conversion fails because the user entered non-numeric input, catch the ValueError exception and display an error message.
# Use an else block that executes only when no exception occurs in the try block.
# Inside the else block, check if the age is greater than or equal to 18.
# If the age is 18 or above, display "You are eligible to vote".
# If the age is below 18, display "You are not eligible to vote".
# The program should handle all types of inputs without crashing.

# Input Format:

# Single line contains the age which can be a number or non-numeric text.

# Output Format:

# If age >= 18: Display "You are eligible to vote".
# If age < 18: Display "You are not eligible to vote".
# If invalid input: Display "Error: Invalid input. Please enter a valid age".

try:
    age = int(input())

except ValueError:
    print("Error: Invalid input. Please enter a valid age")

else:
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
