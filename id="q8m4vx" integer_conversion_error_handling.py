# Write a Python program to accept user input from the console. 
# Try to convert the input into an integer. 
# Handle ValueError if input is not a valid number. 
# Display error messages if conversion fails. 
# If conversion is successful, print the integer value. 
# Ensure the program does not crash for invalid input. 
# Test with multiple user inputs.

try:
    value = int(input())
    print(value)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer")
