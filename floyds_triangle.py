# Write a Python program to print Floyd’s Triangle.
# Use a variable to keep track of the current number.
# The outer loop controls the number of rows.
# The inner loop prints increasing numbers continuously.
# Ensure numbers increment correctly across rows.

n= int(input())
num= 1

for i in range(1, n+1):
    for j in range(i):
        print(num, end= ' ')
        num+= 1
    print()
