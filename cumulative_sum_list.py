# Given a list of numbers, create a new list where each element is the sum of all elements from the original list up to that position.

lst= list(map(int, input().split()))
nlst= []

for i in range(len(lst)):
  nlst.append(sum(lst[:i+1]))

print(nlst)
