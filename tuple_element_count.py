# Write a Python program to count how many times an element appears in a tuple.
# Use the count() method of the tuple.
# Provide the element to be counted.
# Print the total count.

my_tuple = (10, 20, 10, 30, 10, 40)

element = int(input())

count = my_tuple.count(element)

print(count)
