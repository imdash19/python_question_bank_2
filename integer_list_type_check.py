# Write a Python program to create a list containing only integers.
# Store the values in a variable as a list.
# Use the type() function to check the data type.
# Print the type to confirm Python recognizes it as a list.

lst= [int(val) for val in input().split() if val.isdigit()]
print(type(lst))
