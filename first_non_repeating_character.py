# Write a Python program to find the first non-repeating character in a string.
# Accept a string input from the user.
# Use a for loop to check each character’s frequency in the string.
# If a character appears only once, print it and break the loop.
# Use the else block to print a message if all characters repeat.

s= input()
for v in s:
  if s.count(v) == 1:
    print(v)
    break
