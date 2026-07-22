# An online store offers 10% discount on products. 
# Take two prices as input and create a new list with discounted values.

lst= [int(input()), int(input())]
value= [val - (val * 0.1) for val in lst]
print(value)
