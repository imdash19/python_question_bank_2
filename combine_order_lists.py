# Take two items for first order and two for second order. 
# Combine both lists into a single order list.

lst= [val for val in input().split()]
lst1= [val for val in input().split()]
lst2= lst + lst1
print(lst2)
