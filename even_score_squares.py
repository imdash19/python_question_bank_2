# A game system stores scores from 1 to n. It needs squares of only even scores. 
# Take n as input and generate the list.

n= int(input())
lst= []

for i in range(1, n+1):
  if i % 2 == 0:
    lst.append(i ** 2)

print(lst)
