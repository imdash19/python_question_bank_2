# Write a program to determine whether numbers are even or odd.
# The program should accept a space-separated list of integers.
# Each number should be evaluated individually.
# Python’s map() function should be used.
# A lambda expression should apply the condition.
# The output should be a list of strings.

numbers = list(map(int, input().split()))

result = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", numbers))

print(result)
