# Write a Python program to find the greatest common divisor (GCD) of two positive integers.
# The program should ask the user to enter two positive integers
# Use Python’s built-in math.gcd() function to calculate the GCD efficiently.
# Display the result clearly.
# Hint:
# GCD is the largest number that divides both numbers exactly.
# Python provides math.gcd() to make this calculation simple.

import math

num1 = int(input())
num2 = int(input())

result = math.gcd(num1, num2)

print(result)
