# Write a program to use for loop to print the following reverse number pattern:

n= int(input())

for i in range(n, 0, -1):
  for j in range(i, 0, -1):
    print(j, end= ' ')
  print()
