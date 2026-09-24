# Write a program to print numbers from N to 1 using recursion. T
# he program should print the current number and call itself with n-1. 
# Recursion stops when n becomes zero. 
# Output should display numbers in descending order.

def print_numbers(n):
    if n == 0:
        return

    print(n, end=" ")
    print_numbers(n - 1)


n = int(input())

print_numbers(n)
