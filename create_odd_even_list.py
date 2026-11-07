# Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

lst1= list(map(int, input().split()))
lst2= list(map(int, input().split()))

lst= [val for val in lst1 if val%2 == 1] + [val for val in lst1 if val%2 == 0]
print(lst)
