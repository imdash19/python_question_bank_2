# Write a program that takes space-separated integers as input in a single line. Use the reduce() function with a lambda function to calculate the sum of all numbers in the list. The input will be integers separated by spaces, and the output should be a single integer representing the sum of all numbers.

from functools import reduce

numbers = list(map(int, input().split()))

total = reduce(lambda a, b: a + b, numbers)

print(total)
