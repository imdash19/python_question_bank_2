# Write a program to find the largest and smallest digit within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).

n= int(input())
lst= []

while n:
  lst.append(n%10)
  n//= 10

print(max(lst), min(lst))
