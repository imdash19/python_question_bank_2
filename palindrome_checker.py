# Reads a string input and determines whether it is a palindrome (reads the same forwards and backwards). The program performs case-sensitive comparison by default.

s= input()
print('Palindrome' if s == s[::-1] else 'Not Palindrome')
