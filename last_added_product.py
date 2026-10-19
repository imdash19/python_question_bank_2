# You are developing a Shopping Cart Quick View feature for an online store. When customers add multiple items to their cart, they want to quickly see what they added last to make sure it's correct before checking out.Here's how it works:

# A customer adds several products to their shopping cart
# Products are added one by one in a sequence
# The system needs to show the most recently added item for confirmation
# This helps customers verify they added the right product without scrolling through the entire cart
# Example: If a customer's cart contains "Laptop Mouse Keyboard", the most recently added item is "Keyboard", so the system displays: KeyboardYou need to create a program that:

# Takes multiple product names in a single line (separated by spaces)
# Stores them in a list (in the order they were added)
# Accesses and displays only the last item (most recently added product)
# Input Format:

# Single line: Multiple product names separated by spaces
# Output Format:

# Print only the last product name (most recently added item)

products = input().split()

print(products[-1])
