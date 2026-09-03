# Write a Python program to check whether a given element is present in a set.
# The user will first enter all the elements of the set in a single line, separated by spaces.
# Then, the user will enter the element they want to check.
# The program should verify if this element exists in the set.
# If the element is found, print True; otherwise, print False.
# This program helps practice set operations and membership checking using the in keyword.

se= set([val for val in input().split()])
n= input()

print(n in se)
