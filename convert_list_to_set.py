# Write a Python program to convert a list into a set.
# The user enters multiple elements in a single line separated by spaces.
# The list may contain duplicate values.
# The program should convert the list into a set.
# Since sets do not allow duplicate elements, all repeated values should be removed automatically.
# Finally, Set is unordered and the result will change So convert the set again in to list using sorted funcion then print the resut.

lst= set(map(int, input().split()))
lst= list(lst)
lst.sort()
print(lst)
