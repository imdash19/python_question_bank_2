# Write a Python program to read a string.
# Check whether none of the vowels exist in the string.
# If no vowels are present, print True.
# Otherwise, print False.

s= input()
res= True

for v in s:
  if v.lower() in 'aeiou':
    res= False
    break

print(True if res else False)
