# A store maintains a price list [100,200,300]. 
# The first value represents the main product. 
# Take a new price as input and update the first element. 
# Print the updated list.

prices = [100, 200, 300]

new_price = int(input())

prices[0] = new_price

print(prices)
