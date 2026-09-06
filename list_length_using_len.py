# Write a Python program that reads multiple integers and stores them in a list.
# The input values are given in a single line separated by spaces.
# Use the built-in len() function to find the number of elements in the list.
# Do not manually count the elements.
# Read the input from standard input.
# Store all values in a list before processing.
# Print the total count of elements.
# The output should be an integer value.

numbers = list(map(int, input().split()))

print(len(numbers))
