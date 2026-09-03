# Write a Python program to add a new element to an existing set.
# The user will enter the initial elements of the set in a single line, separated by spaces.
# Then, the user will enter the element to add.
# The program should insert the new element into the set using the add() method.
# Print the updated set showing the newly added element.
# This program helps practice modifying sets and understanding that sets store unique elements.

se= set(input().split())
se.add(input())
print(se)
