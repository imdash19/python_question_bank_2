# Write a Python program that accepts multiple integers as input.
# The input is provided as space-separated values in one line.
# Use the built-in max() function to find the largest number.
# Do not use loops for comparison.
# The list may contain positive and negative numbers.
# Store the input values in a list.
# Print the maximum value from the list.
# Ensure correct output for mixed values.

numbers = list(map(int, input().split()))

print(max(numbers))
