# Write a Python program that accepts multiple integers as input.
# The input values are space-separated in a single line.
# Use the built-in sum() function to calculate the total.
# Do not use loops for addition.
# Store all values in a list before processing.
# The list may contain negative numbers.
# Print the total sum of elements.
# The output should be a single integer.

lst= list(map(int, input().split()))
print(sum(lst))
