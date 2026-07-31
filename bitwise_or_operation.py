# Write a Python program to read two integers.
# Apply the bitwise OR (|) operator on the given numbers.
# Compare each bit position of both numbers.
# A bit becomes 1 if at least one corresponding bit is 1.
# Print the final result.

n1, n2= int(input()), int(input())
res= n1 | n2
print(res)
