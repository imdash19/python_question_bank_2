# Write a program to find the maximum digit in each number.
# The program should accept a space-separated list of numbers as strings.
# Each number should be evaluated digit by digit.
# Python’s map() function should be used.
# The maximum digit of each number should be returned.
# The output should be a list of digits.

numbers = input().split()

maximum_digits = list(map(lambda x: max(map(int, x)), numbers))

print(maximum_digits)
