# Write a Python program to sort tuples inside a list based on the secondt element of each tuple.
# Create a List with values [(1, 3), (2, 1), (3, 2)]
# Use the sorted() function with a suitable key to sort the list of tuples in ascending order based on the second value.
# Finally, print the sorted list of tuples in Python list format.

tuples_list = [(1, 3), (2, 1), (3, 2)]

sorted_list = sorted(tuples_list, key=lambda x: x[1])

print(sorted_list)
