# Write a Python program to take three numbers as input.
# Identify the largest number first.
# Ignore the highest value and compare the remaining two.
# Print the second largest number.

n1, n2, n3 = int(input()), int(input()), int(input())

if (n1 >= n2 and n1 <= n3) or (n1 <= n2 and n1 >= n3):
    print(n1)
elif (n2 >= n1 and n2 <= n3) or (n2 <= n1 and n2 >= n3):
    print(n2)
else:
    print(n3)
