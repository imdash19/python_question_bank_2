# Write a Python program which reads list of elements and to remove a specific value from a list.
# Use the remove() method with the value to delete.
# Ensure only the first occurrence of the value is removed.
# Print the updated list to show the element has been deleted.

lst= [val for val in input().split()]
lst.remove(input())
print(lst)
