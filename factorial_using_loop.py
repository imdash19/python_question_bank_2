# Write a program to use a loop to find the factorial of a given number (e.g., 5!). The factorial of N is the product of all integers from 1 to N.

n= int(input())
fact= 1

if n == 0 or n == 1:
  print(fact)

elif n > 1:
  for i in range(2, n+1):
    fact*= i

  print(fact)
