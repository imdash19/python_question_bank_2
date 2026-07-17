# An order system stores each order as [item, quantity]. 
# Take two orders as input and store them as nested lists.
# Print the structure.

order= [int(val) if val.isdigit() else val for val in input().split()]
order= [order[i:i+2] for i in range(0, len(order)-1, 2)]
print(order)
