# Write a Python program to read a string.
# Check whether the string contains any digit from 0 to 9.
# If any digit is found, print Yes.
# Otherwise, print No.

s= input()
for v in s:
    if v.isdigit():
        print('Yes')
        break
else:
    print('No')
