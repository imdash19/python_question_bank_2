# Write a program that takes two numbers as input in a single line separated by space. Use a lambda function to find and print the maximum of the two numbers. The input will be two integers separated by a space, and the output should be the larger of the two numbers. If both numbers are equal, print that number.

max_num= lambda x, y: x if x>y else y
x, y= map(int, input().split())
print(max_num(x, y))
