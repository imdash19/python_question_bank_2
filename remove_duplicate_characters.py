# Write a Python program to read a string as input.
# Remove duplicate characters while keeping the original order.
# Process each character only once.
# Create a new string without repeated characters.
# Print the final modified string.

ns= ''
s= input()

for i in range(len(s)):
  if i not in ns:
    ns+= i

print(ns)
