# Write a Python program which takes tuple of elements as input and  locate the first occurrence of an element in a tuple.
# Use the index() method and provide the element.
# Store or directly print the returned index.
# Handle cases where the element might not exist.

elements = tuple(input().split())
element = input()

if element in elements:
    index = elements.index(element)
    print(index)
else:
    print("Element not found")
