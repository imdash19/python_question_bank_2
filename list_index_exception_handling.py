# Write a Python program to accept an index number from the user. 
# Use a predefined list of elements in your program. 
# elements = ["apple", "banana", "cherry", "date", "elderberry"]
# Try to access the element at the given index. 
# Handle cases where the index is out of range. 
# Handle invalid input where the user enters non-integer values. 
# Display appropriate messages for errors. 
# If the input is valid and index exists, print the element.

elements = ["apple", "banana", "cherry", "date", "elderberry"]

try:
    index = int(input())
    print(elements[index])

except IndexError:
    print("Error: Index out of range")

except ValueError:
    print("Error: Invalid input. Please enter an integer")
