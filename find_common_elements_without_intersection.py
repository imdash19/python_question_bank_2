# Given two lists, find the elements that appear in both. Do not use Python’s built-in set().intersection() method.

lst1= list(map(int, input().split()))
lst2= list(map(int, input().split()))
lst= []

for val in lst1:
  if val in lst2:
    lst.append(val)

print(lst)
