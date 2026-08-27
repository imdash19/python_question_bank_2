# Write a Python program to eliminate repeated elements in a list.
# Use a loop or set() to track unique elements.
# Preserve the original order if needed.
# Print the final list with only distinct elements.

lst= list(input().split())
olst= []
for val in lst:
    if val not in olst:
        olst.append(val)
print(olst)
