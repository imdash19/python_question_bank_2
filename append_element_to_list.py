# Write a Python program to take a list of integer elements.
# Accept a new element to be added at the end.
# Use the append() method to insert the element.
# Print the updated list showing the new element at the last position.

lst= list(map(int, input().split()))
lst.append(int(input()))
print(lst)
