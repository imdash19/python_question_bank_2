# Write a program that takes space-separated integers as input in a single line. Use the filter() function with a lambda function to filter only the odd numbers from the list. The input will be integers separated by spaces, and the output should be the list of odd numbers in the same order.

numbers = list(map(int, input().split()))

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)
