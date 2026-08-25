# Write a Python program to read list of elements and a new element.
# Take the position (index) where the element should be inserted.
# Use the insert() method with the index and element.
# Print the updated list to display the inserted element at the correct position.

lst= [val for val in input().split()]
n= input()
i= int(input())
lst.insert(i, n)
print(lst)
