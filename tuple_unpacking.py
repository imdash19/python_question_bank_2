# Write a Python program to read a tuple with exactly two values.
# Assign the first value to variable a.
# Assign the second value to variable b.
# Print the values of a and b in the same order.

t= tuple(int(input()), int(input()))
print(*t)
