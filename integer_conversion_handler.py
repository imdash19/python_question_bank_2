# Write a Python program to accept user input from console and handle conversion errors.Here's what you need to do:
# Take an input value from the user which could be anything like a number or text.
# Use a try block to attempt converting the input into an integer.
# If the conversion is successful, display the converted number with a success message.
# Use an except block to catch the ValueError exception that occurs when the input cannot be converted to an integer.
# If the conversion fails, display a clear error message asking the user to enter a valid number.
# The program should handle any type of input without crashing.
# Input Format:
# Single line contains any value which can be numeric or non-numeric text.
# Output Format:
# If valid numeric input: Display "Successfully converted: [number]".
# If non-numeric input: Display "Error: Invalid input. Please enter a valid integer".

try:
    value = input()
    number = int(value)
    print("Successfully converted:", number)

except ValueError:
    print("Error: Invalid input. Please enter a valid integer")
