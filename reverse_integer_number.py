# Write a program to reverse a given integer number (e.g., 76542 should become 24567).

n= int(input())
nn= 0

while n:
  nn= (nn*10) + (n%10)
  n//=10

print(nn)
