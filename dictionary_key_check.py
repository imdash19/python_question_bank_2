# Write a Python program to create a dictionary.
# Creates a dictionary with some predefined key-value pairs (for example: 'name', 'dept', 'salary').

# Accepts a key as input from the user.
# Checks if the key exists in the dictionary.
# Prints:

# "Key found" if the key exists.

# "Key not found" if the key does not exist.

# This exercise helps you understand dictionary membership and how to check for keys in Python.

d= {'name': 'Bibhuti', 'dept': 'python', 'salary': 39069.5}
k= input()

if k in d:
  print('Key found')
else:
  print('Key not found')
