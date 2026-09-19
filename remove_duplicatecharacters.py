# Write a Python program to remove duplicate characters from a string while maintaining the original order. 
# The program should accept a string from the user. 
# Case should be preserved. Only first occurrence of each character should remain. 
# Output should display the cleaned string.

s= input()
ns= ''
for v in s:
    if v not in ns:
        ns+= v

print(ns)
