# Write a Python program to accept a string input.
# Use list comprehension to convert each character to its ASCII value.
# Apply the ord() function to each character.
# Store all ASCII values in a list.
# Print the resulting list.

text = input()

ascii_values = [ord(char) for char in text]

print(ascii_values)
