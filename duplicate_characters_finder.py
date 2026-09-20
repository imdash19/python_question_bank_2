# Write a Python program to find all duplicate characters in a string. The program should accept a string input.
# Output should list characters that appear more than once.
# Case should be preserved. Spaces should be ignored.

s= input()
ns= ''
for v in s:
    if s.count(v) > 1 and v not in ns:
        ns+= v
        ns+= ' '

print(ns)
