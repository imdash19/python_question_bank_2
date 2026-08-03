# Write a Python program to create a dictionary with keys name and age.
# Assign appropriate values to these keys.
# Store the dictionary in a variable.
# Prints the dictionary in the format {'name':'Name','age':Age} (no spaces after colons).
# This exercise helps you understand Python dictionaries, key-value pairs, and basic data storage.

name = input()
age = int(input())

data = {"name": name, "age": age}

print(f"{{'name':'{data['name']}','age':{data['age']}}}")
