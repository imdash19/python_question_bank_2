# Write a Python program to accept a string containing spaces.
# Use a string method to replace all spaces with underscores (_).
# Ensure every space in the string is replaced correctly.
# Store the modified string in a new variable.
# Print the updated string clearly.

s= input()
ns=''
for i in range(len(s)):
    if s[i] == ' ':
        ns+= '_'
    else:
        ns+= s[i]

print(ns)
