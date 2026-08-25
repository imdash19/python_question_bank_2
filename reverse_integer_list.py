# Write a Python program which accepts list of integers and reverse the order of elements in a list.
# Use the reverse() method or slicing to reverse the list.
# Print the reversed list to show the elements in opposite order.

lst= list(map(int, input().split()))
print(lst[::-1])
