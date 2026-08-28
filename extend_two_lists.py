# Write a Python program to accept two lists from the user.
# Use the extend() method to add all elements from the second list to the first.
# Store the combined list.
# Print the updated list showing all elements.

lst1= list(input().split())
lst2= list(input().split())
lst1+= lst2

print(lst1)
