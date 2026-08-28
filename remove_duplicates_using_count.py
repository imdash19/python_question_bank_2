# Write a Python program to accept a list and an element to check.
# Use the count() method to find how many times the element appears.
# Store the count in a variable.
# Print the count clearly with the element mentioned.

lst= list(input().split())
n= input()

print(f'{n} appears {lst.count(n)} times')
