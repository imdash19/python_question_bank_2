# Write a Python program to print a diamond pattern using *.
# First, print an increasing pyramid of stars.
# Then, print a decreasing pyramid below it.
# Use nested loops for spaces and stars.
# Ensure the diamond shape is symmetric.

rows = int(input())

# Upper half
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
