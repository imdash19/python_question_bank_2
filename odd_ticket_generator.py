# A ticketing system generates odd-numbered tickets only. 
# Take n as input and generate a list of odd numbers up to n.

n= int(input())
lst= []

for i in range(1, n+1):
  if i % 2 == 1:
    lst.append(i)

print(lst)
