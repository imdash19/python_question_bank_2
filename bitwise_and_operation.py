# Write a Python program to read two integers.
# Apply the bitwise AND (&) operator on the given numbers.
# Compare each bit of both numbers one by one.
# A bit becomes 1 only when both corresponding bits are 1.
# Print the final result after the operation.

n1, n2= int(input()), int(input())
res= n1 & n2
print(res)
