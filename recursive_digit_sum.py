# Write a program to find the sum of digits of a given number using recursion. 
# The program should take an integer as input from the user. 
# It should repeatedly extract the last digit and add it to the sum. 
# The recursion should stop when the number becomes zero.
# Built-in recursion logic must be used.

def digit_sum(number):
    if number == 0:
        return 0
    return number % 10 + digit_sum(number // 10)


number = int(input())

if number < 0:
    number = -number

print(digit_sum(number))
