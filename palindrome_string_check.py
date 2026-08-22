# Write a Python program to accept a string from the user.
# Reverse the string using slicing or a loop.
# Compare the original string with the reversed string.
# Check whether both values are the same.
# Print whether the string is a palindrome or not.

s= input()
print('Yes, it is a palindrome' if s == s[::-1] else 'No, it is not a palindrome')
