# Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.

s= int(input())

for v in s:
  if v.isdigit():
    print('Yes, string contains digit')
    break
else:
  print('No, string doesn't contains any digit')
