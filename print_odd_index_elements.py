# Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).

lst= list(map(int, input().split()))
for i in range(len(lst)):
  if i % 2 == 1:
    print(lst[i])
