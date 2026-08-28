# Write a Python program to generate numbers in a given range.
# Use list comprehension to create tuples of number and its square.
# Format each tuple as (number, square).
# Store all tuples in a list.
# Print the list of tuples.

lst= list(map(int, input().split()))
n1, n2= lst[0], lst[1]
lst1= []

for i in range(n1, n2+1):
    lst1.append((i, i**2))

print(lst1)
