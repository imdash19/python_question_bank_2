# Accepts a dictionary as input from the user in the standard Python format.
# Example: {'a':10,'b':20,'c':30}
# Calculates the sum of all values in the dictionary.
# Prints the total sum.
# This exercise helps beginners practice dictionaries, data types, and basic numeric operations in Python.
# Note: use import ast  and literal_eva method

import ast

data = ast.literal_eval(input())

total = sum(data.values())

print(total)
