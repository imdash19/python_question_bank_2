# Write a Python program to accept a list of strings.
# Use list comprehension to convert each string to uppercase.
# Apply the upper() method on every element.
# Store the converted strings in a new list.
# Print the updated list.

numbers = list(map(int, input().split()))

count = 0

for number in numbers:
    count += 1

print("Length:", count)
