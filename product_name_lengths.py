# An inventory system needs the length of product names. 
# Take two product names and generate a list containing their lengths.

product= [val for val in input().split()]
product_len= [len(val) for val in product]

print(product_len)
