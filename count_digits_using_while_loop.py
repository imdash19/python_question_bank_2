# Write a program to count the total number of digits in a given integer using a while loop.

n= int(input())
tn= 0

while n:
  n= n//10
  tn+= 1

print(tn)
