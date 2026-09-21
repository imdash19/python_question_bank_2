# Write a Python program to access multiple elements from a list using given indices.
# The program should accept a space-separated list of elements from the user.
# It should then accept a space-separated list of indices.
# Use Python list comprehension to fetch elements present at those indices.
# Display the result as a new list.

elements = input().split()
indices = list(map(int, input().split()))

result = [elements[i] for i in indices]

print(result)
