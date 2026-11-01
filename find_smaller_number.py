# Write a Python program to read two numbers.
# Compare both numbers to find the smaller one.
# Print the smaller value.
# If both are equal, print that value.

n1, n2= int(input()), int(input())
print(n1 if n1 <= n2 else n2)
