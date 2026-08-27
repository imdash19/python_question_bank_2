# Write a Python program to arrange the elements of a list in decreasing order.
# Use the sort(reverse=True) method to sort in descending order.
# Print the sorted list to display elements from largest to smallest.

lst= list(map(int, input().split()))
lst.sort(reverse= True)
print(lst)
