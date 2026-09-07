# Write a recursive function to count the number of digits in a given number.
# The input is a single integer.
# Reduce the number by dividing it by 10 in each call.
# Define a base condition to stop recursion.
# Do not use loops or string conversion.
# Return the digit count.
# Print the final result.
# Ensure zero is handled correctly.

def count_digits(n):
    if n == 0:
        return 1
    if n < 0:
        n = -n
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

number = int(input())
print(count_digits(number))
