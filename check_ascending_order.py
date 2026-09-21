# Write a Python program to check whether a list is sorted in ascending order.
# The program should accept a space-separated list of numbers from the user.
# It should compare consecutive elements of the list.
# Use Python’s built-in zip() and all() functions.
# If the list is sorted in ascending order, print TRUE; otherwise, print FALSE.

numbers = list(map(int, input().split()))

if all(a <= b for a, b in zip(numbers, numbers[1:])):
    print("TRUE")
else:
    print("FALSE")
