# Write a Python program to calculate the total cost of a coffee order based on the type of coffee and whether an extra shot is added.
# Pricing:
# "Espresso" → ₹50
# "Latte" → ₹80
# "Cappuccino" → ₹70
# Extra shot → add ₹20

# Input Format:
# String: coffee_type
# Boolean: extra_shot

# Output Format:
# Print: Total: ₹amount

coffee_type = input()
extra_shot = input() == "True"

if coffee_type == "Espresso":
    total = 50
elif coffee_type == "Latte":
    total = 80
elif coffee_type == "Cappuccino":
    total = 70

if extra_shot:
    total += 20

print("Total: ₹", total)
