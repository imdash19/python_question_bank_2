# Write a Python program to display all even numbers between 1 and 50.
# Use a for loop to iterate through the range of numbers.
# Check each number to determine if it is even.
# Print only the numbers that satisfy the even condition.
# Ensure the output contains only even values.

lst= [i for i in range(1, 51) if i % 2 == 0]
print(*lst)
