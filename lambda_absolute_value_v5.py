# Write a program that takes two integers as input in a single line separated by space. Use a lambda function to calculate and print their sum. The input will be two integers (can be positive or negative) separated by a space, and the output should be a single integer representing their sum.

absolute = lambda x: x if x >= 0 else -x

number = int(input())
print(absolute(number))
