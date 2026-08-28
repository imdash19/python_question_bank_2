# Write a Python program to accept a list and an element to find.
# Use the index() method to locate the first occurrence.
# Store the index in a variable.
# Print the index clearly.

lst= list(input().split())
n= input()

print(f'Index of {n}: {lst.index(n)}')
