# Write a Python program to find the difference between consecutive numbers in a given list.
# The program should ask the user to enter a space-separated list of numbers.
# Convert the input into integers.
# Use Python’s zip() and list comprehension to compute the differences efficiently.
# Display the differences as a new list.
# Hint:
# If the list is [a, b, c, d], the differences are [b-a, c-b, d-c].
# zip(list[:-1], list[1:]) pairs consecutive elements together.

numbers = list(map(int, input().split()))

differences = [b - a for a, b in zip(numbers[:-1], numbers[1:])]

print(differences)
