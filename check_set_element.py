# Write a Python program to check whether a given element exists in a set.
# The program should read a group of elements and store them in a set.
# Then, it should read another input value to be checked.
# If the element is found in the set, display that it is present.
# Otherwise, display that the element is not present.
# The comparison should work for numbers or strings entered by the user.

elements = input().split()

my_set = set(elements)

element = input()

if element in my_set:
    print("Present")
else:
    print("Not Present")
