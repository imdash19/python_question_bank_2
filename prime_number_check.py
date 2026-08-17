# Write a Python program to check whether a given number is prime.
# Accept an integer input from the user.
# Use a while loop to test divisibility starting from 2.
# If the number is divisible by any value, break the loop.
# Use the else block to confirm the number is prime if no break occurs.
# Print whether the number is prime or not.

n= int(input())

if n < 2:
    print('Not Prime')

else:
    for i in range(2, n):
        if n % i == 0:
            print('Not Prime')
            break
    else:
        print('Prime')
