# An order system stores each order as (item, quantity). 
# Take two orders as input and store them as nested tuples. 
# Print the structure.

order= []
for i in range(2):
  tup= (input(), int(input()))
  order.append(tup)

order= tuple(order)
print(order)
