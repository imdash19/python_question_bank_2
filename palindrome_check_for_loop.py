# Write a Python program to check whether a string is a palindrome.
# Accept a string input from the user.
# Use a for loop to reverse the string.
# Compare the reversed string with the original.
# Print whether the string is a palindrome or not.

s= input()
print('Palindrome' if s == s[::-1] else 'Not a Palindrome')
