# A store wants to add index-based service charges to prices. 
# Take two prices and add index value to each element using list comprehension.

price= list(map(int, input().split()))
updated_price= [price[val] + val for val in range(len(price))]
print(updated_price)
