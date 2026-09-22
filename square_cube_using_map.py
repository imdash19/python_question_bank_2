# Write a program to apply multiple operations on each element of a list.
# The program should accept a space-separated list of integers from the user. 
# It should calculate the square and cube of every number.
# The program must use Python built-in map() function.
# Lambda expressions should be used for processing values.
# The final output should be a list of tuples containing square and cube values.

numbers = list(map(int, input().split()))

result = list(map(lambda x: (x ** 2, x ** 3), numbers))

print(result)
