# Write a Python program to accept a string from the user.
# Use a loop to process each character in the string.
# Convert each character to its ASCII value using a function.
# Print the character along with its ASCII value.
# Ensure the output is easy to read.

s= input()

for v in s:
    print(f"{v}:{ord(v)}", end= ' ')
