# Create a function that accepts variable length arguments and returns
# the maximum value. The inputs are integers entered one per line.
# The function should correctly identify the largest number. 
# This program demonstrates how multiple values can be compared 
# using *args. Handle both positive and negative numbers.

def find_max(*args):
    return max(args)


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = find_max(num1, num2, num3)

print(result)
