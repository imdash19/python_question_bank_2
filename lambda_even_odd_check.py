# Write a program that takes a single integer as input. Use a lambda function to check whether the number is even or odd. The input will be one integer, and the output should be True if the number is even, or False if the number is odd.

even_or_odd= lambda x: True if x % 2 == 0 else False
print(even_or_odd(int(input())))
