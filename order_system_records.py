# An order system stores each order as [item, quantity]. 
# Take two orders as input and store them as nested lists.
# Print the structure.

orders= [int(val) if val.isdigit() else val for val in input().split()]
paired_list= [list(orders[i:i+2]) for i in range(0, len(orders)-1, 2)]
print(paired_list)
