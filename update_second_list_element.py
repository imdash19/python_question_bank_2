# Write a Python program to work with a list having at least two elements.
# Change the second element of the list to 20.
# Remember that list indexing starts from 0.
# Print the updated list.

lst= list(map(int, input().split()))
lst[1]= 20
print(lst)
