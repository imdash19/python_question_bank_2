# Write a recursive function to calculate the factorial of a given number.
# The input is a single non-negative integer.
# The function should call itself repeatedly.
# Define a proper base condition to stop recursion.
# Do not use loops for calculation.
# Return the factorial value from the function.
# Print the final result.
# Ensure correct output for input value zero.

n= int(input())

if n > 0:
    def fact(n):
        if n == 1:
            return 1

        return n * fact(n-1)

print(fact(n))
