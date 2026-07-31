# Write a program that takes a number and a position value i from the user
# Clear all bits from position 0 (LSB) up to position i in that number
# All bits beyond position i should remain the same
# Display the final result after clearing the bits
# This uses bitwise operations to modify specific bits in a number

n, i= int(input()), int(input())
result = n & (~((1 << (i + 1)) - 1))
print(result)
