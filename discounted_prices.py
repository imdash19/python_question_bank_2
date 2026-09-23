# Write a program to calculate discounted prices.
# The program should accept a space-separated list of prices.
# A fixed discount percentage should be applied.
# # Fixed discount percentage 
# discount = 10 # 10%
# Python’s map() function should be used.
# Each price should be reduced based on the discount.
# The output should be a list of discounted prices.

discount = 10

prices = list(map(float, input().split()))

discounted_prices = list(map(lambda price: price - (price * discount / 100), prices))

print(discounted_prices)
