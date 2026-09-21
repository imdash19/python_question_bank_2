# The program should ask the user to enter two positive integers.
# Use Python’s built-in math.lcm() function to calculate the LCM efficiently.
# Display the result clearly.
# Hint:
# LCM is the smallest number divisible by both numbers.
# Python 3.9+ provides math.lcm() which makes this task very simple.

import math

num1 = int(input())
num2 = int(input())

result = math.lcm(num1, num2)

print(result)
