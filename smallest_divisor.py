# Write a Python program to find the smallest divisor of a number.
# Accept an integer greater than or equal to 2 from the user.
# Use a while loop starting from 2 to check divisibility.
# If a divisor is found, print it and break the loop.
# Use the else block if no divisor is found within the loop range.
# Print the smallest divisor clearly.

n= int(input())

for i in range(2, n):
    if n % i ==0:
        print('Smallest Divisor: ', i)
        break
