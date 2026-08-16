# Write a Python program to print all odd numbers between 1 and 50.
# Initialize a variable with the value 1.
# Use a while loop to check numbers up to 50.
# Increment the number by 2 in each iteration.
# Print each odd number in the loop.

# Write your code here

n= 1

while n <= 50:
    if n % 2 == 1:
        print(n, end= ' ')
    n+= 1
