# Write a Python program to calculate the sum of elements entered by the user.
# The user enters space-separated numeric values in a single line.
# Convert the input into a tuple and use the sum() function to find the total.
# Print the sum of all elements.

numbers = tuple(map(float, input().split()))

total = sum(numbers)

print(total)
