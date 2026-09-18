# Write a Python program to remove the i’th character from a string. 
# The program should accept a string and an index from the user.
# Indexing starts from zero. If the index is valid, remove the character. 
# If invalid, print the original string. The updated string should be displayed.

s= input()
i= int(input())

s= s[:i]+s[i+1:]
print(s)
