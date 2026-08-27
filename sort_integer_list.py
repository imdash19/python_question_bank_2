# Write a Python program to arrange the elements of a list in increasing order.
# Use the sort() method to sort the list.
# Print the sorted list to show all elements from smallest to largest.

lst= list(map(int, input().split()))
lst.sort()
print(lst)
