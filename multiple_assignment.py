# Write a Python program with three variables having initial values.
# Reassign all three variables to the value 99 at the same time.
# Use multiple assignment in one statement.
# Print all three variable values.

n1, n2, n3= input().split()
n1, n2, n3= int(n1), int(n2), int(n3)
n1, n2, n3= 99, 99, 99

print(n1, n2, n3)
