# A store price list is [100,200,300]. 
# Take two new prices and replace the first two elements. 
# Print updated list.

prices = [100, 200, 300]

price1 = int(input())
price2 = int(input())

prices[0:2] = [price1, price2]

print(prices)
