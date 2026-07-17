# A store wants to add index-based service charges to prices. 
# Take two prices and add index value to each element using list comprehension.

prices = [int(val) for val in input().split()]

updated_prices = [price + index for index, price in enumerate(prices)]

print(updated_prices)
