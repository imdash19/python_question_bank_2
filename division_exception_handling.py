# Write a Python program to perform division with proper error handling for multiple exception types.Here's what you need to do:
# Take two numbers as input from the user on separate lines.
# The first number will be the dividend (the number to be divided).
# The second number will be the divisor (the number to divide by).
# Use a try block to convert both inputs to float numbers and perform the division operation.
# Handle the ZeroDivisionError exception that occurs when the user tries to divide by zero and display an appropriate error message.
# Handle the ValueError exception that occurs when the user enters non-numeric input like letters or symbols and display an error message.
# If both inputs are valid numbers and the divisor is not zero, perform the division and display the result.
# The program should handle all types of errors gracefully without crashing.
# Input Format:
# First line contains the dividend which can be a number or non-numeric text.
# Second line contains the divisor which can be a number or non-numeric text.
# Output Format:
# If division succeeds: Display "Result: [quotient]".
# If divisor is zero: Display "Error: Cannot divide by zero".
# If non-numeric input: Display "Error: Invalid input. Please enter valid numbers".

try:
    dividend = float(input())
    divisor = float(input())

    result = dividend / divisor
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input. Please enter valid numbers")
