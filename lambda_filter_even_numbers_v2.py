# Write a program that takes space-separated integers as input in a single line. Use the filter() function with a lambda function to filter only the even numbers from the list. The input will be integers separated by spaces, and the output should be the list of even numbers in the same order.

numbers = list(map(int, input().split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
