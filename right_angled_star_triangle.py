# Write a Python program to print a right-angled triangle pattern using *.
# Accept the number of rows as input from the user.
# Use an outer loop to control the number of rows printed.
# Use an inner loop to print stars based on the current row number.
# Ensure each row appears on a new line forming a triangle shape.

n= int(input())

for i in range(1, n+1):
    print('*' * i)
