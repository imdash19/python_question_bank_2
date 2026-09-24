# Write a program to print numbers from 1 to N using recursion.
# The program should accept a positive integer as input.
# It should first call the recursive function with n-1. After returning, 
# it should print the current number. 
# This ensures numbers are printed in ascending order. 
# Recursion stops when n becomes 0.

def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n, end=" ")


n = int(input())

print_numbers(n)
