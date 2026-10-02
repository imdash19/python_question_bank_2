# Reads a string containing comma-separated integers and converts it into a list of integer values. Useful for processing CSV-like data where numbers are separated by commas.

numbers = list(map(int, input().split(",")))

print(numbers)
