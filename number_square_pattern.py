# Write a Python program to print a square pattern of numbers.
# Use nested loops where the outer loop controls the row number.
# Repeat the same number across each row using the inner loop.
# Ensure the pattern displays four rows and four columns.
# Each row should contain the same repeated number.

n= int(input())

for i in range(1, n+1):
    for j in range(n):
        print(i, end= ' ')
    print()
