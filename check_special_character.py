# Write a Python program to read a password string.
# Check if it contains any special character from !@#$%^&*.
# If found, print True.
# Otherwise, print False.

s= input()
for v in s:
  if v in '!@#$%^&*':
    print('Yes')
    break
else:
  print('No')
