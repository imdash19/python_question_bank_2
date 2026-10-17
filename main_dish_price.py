# You are building a Restaurant Billing System where customers order multiple items. The restaurant wants to highlight the price of the main dish (first item ordered) separately on the receipt for promotional purposes.
# Here's how it works:

# A customer orders multiple items, each with a different price
# The prices are entered together in order (main dish first, then sides/drinks)
# The system needs to extract and display the price of the first item (main dish)
# This helps the restaurant track which main dishes are popular

# Example: If a customer orders items priced at "250 50 80" (Main dish $250, Side $50, Drink $80), the system should display the main dish price: 250
# You need to create a program that:

# Takes multiple prices in a single line (separated by spaces)
# Stores them in a list
# Accesses and displays only the first price (main dish price)

# Input Format:

# Single line: Multiple prices (integers) separated by spaces

# Output Format:

# Print only the first price (main dish price)

prices = list(map(int, input().split()))

print(prices[0])
