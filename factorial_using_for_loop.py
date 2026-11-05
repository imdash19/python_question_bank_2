# Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

n= int(input())
fact= 1

if n >=0:
  if n == 0 or n == 1:
    print(fact)
  else:
    for i in range(2, n+1):
      fact*= i
    print(fact)
