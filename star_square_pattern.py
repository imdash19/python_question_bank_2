# Write a Python program to print a square pattern using *.
# Use an outer loop to control the number of rows.
# Use an inner loop to print stars in each row.
# Ensure every row has the same number of stars.
# Print the pattern in a clear square shape.

n= int(input())

for i in range(n):
    for j in range(n):
        print('*', end= ' ')
    print()
