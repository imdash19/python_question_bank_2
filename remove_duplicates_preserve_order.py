# Write a program to remove all duplicate values from a list using a loop, maintaining the original order of elements.

lst= list(map(int, input().split()))
new_list= []

for val in lst:
  if val not in new_list:
    new_list.append(val)

print(new_list)
