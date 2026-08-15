# Write a Python program to print numbers from 1 to a given value n.
# Take an integer n as input from the user.
# Use a for loop to iterate from 1 to n.
# Print each number during every iteration of the loop.
# Ensure the numbers are displayed in sequence.

n= int(input())

for i in range(1, n+1):
    print(i, end=' ')
