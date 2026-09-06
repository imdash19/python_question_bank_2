# Write a Python program that reads integers from the user.
# The input values are entered in one line separated by spaces.
# Use the built-in min() function to find the smallest number.
# Do not use conditional statements for comparison.
# Handle the case where only one value is provided.
# Store the input values in a list.
# Print the minimum value.
# Ensure correct output for all valid inputs.

numbers = list(map(int, input().split()))

print(min(numbers))
