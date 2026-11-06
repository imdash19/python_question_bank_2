# Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

def func(lst):
  return lst[0] == lst[-1]

lst= input().split()
print(func(lst))
