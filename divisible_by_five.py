# Iterate through a given list of numbers and print only those numbers which are divisible by 5.

lst= list(map(int, input().split()))
for val in lst:
  if val%5 == 0:
    print(val)
