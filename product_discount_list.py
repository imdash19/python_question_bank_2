# An online store offers 10% discount on products. 
# Take two prices as input and create a new list with discounted values.

lst= [int(val) for val in input().split()]

lst= [int(val - val / 10) for val in lst]

print(lst)
