# Write a Python program to perform the union operation on two sets.
# The program should read elements of two sets entered by the user.
# All elements from both sets should be combined.
# Duplicate values must appear only once.
# Since sets are unordered, convert the result into a sorted list before printing.

set1 = set(input().split())
set2 = set(input().split())

union_set = set1.union(set2)

result = sorted(union_set)

print(result)
