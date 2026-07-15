# A cart quantity list is [2,3]. 
# Take two new quantities and replace both values. 
# Print updated list.

quantities = [2, 3]

quantity1 = int(input())
quantity2 = int(input())

quantities[:] = [quantity1, quantity2]

print(quantities)
