# Write a program that takes space-separated integers as input in a single line. Use the filter() function with a lambda function to filter only the non-zero numbers from the list. The input will be integers separated by spaces, and the output should be the list of non-zero numbers (both positive and negative) in the same order.

lst= list(map(int, input().split()))
non_xero= list(filter(lambda x: x != 0, lst))
print(non_xero)
