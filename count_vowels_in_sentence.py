# Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

s= int(input())
vowels= 0

for v in s:
  if v.lower() in 'aeiou':
    vowels+= 1

print(vowels)
