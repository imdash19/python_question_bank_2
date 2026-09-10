# Write a program that takes space-separated words as input in a single line. Use the reduce() function with a lambda function to concatenate all words into a single string with spaces between them. The input will be words separated by spaces, and the output should be all words joined together with single spaces maintaining the original order.

from functools import reduce

words = input().split()

result = reduce(lambda a, b: a + " " + b, words)

print(result)
