# Write a Python program to reverse each word in a given string. 
# The program should take a sentence as input.
# Word order must remain unchanged. 
# Only characters inside words should be reversed. 
# Spaces must be preserved. 
# The output should show the modified sentence clearly.

s= input().split()

for v in s:
    print(v[::-1], end= ' ')
