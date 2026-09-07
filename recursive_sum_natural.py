# Write a recursive function to calculate the sum of the first N natural numbers.
# The input is a single integer N.
# Reduce the problem size in each recursive call.
# Define a base condition to stop recursion.
# Do not use loops or built-in sum functions.
# Return the calculated sum.
# Print the final result.
# Ensure correct handling of small input values.

def cal_sum(n):
    if n == 0:
        return 0

    return n + cal_sum(n-1)

print(cal_sum(int(input())))
