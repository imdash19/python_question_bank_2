# Write a Python program which reads list of elements and to delete an element using its index.
# Accept the index of the element to remove.
# Use the pop() method with the index to delete it.
# Print the updated list to show the deletion effect.

lst= [val for val in input().split()]
lst.pop(int(input()))
print(lst)
