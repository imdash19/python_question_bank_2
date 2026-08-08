# Write a Python program to take three numbers as input.
# Compare all three numbers using conditional statements.
# Check which number is greater than the other two.
# Print the largest number among the three.

n1, n2, n3= int(input()), int(input()), int(input())
print(n1 if n1 >= n2 and n1 >= n3 else n2 if n2 > n1 and n2 >= n3 else n3)
