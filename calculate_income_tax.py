# Calculate income tax for a given income based on these rules:

# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax

income = float(input())

if income <= 10000:
    tax = 0
elif income <= 20000:
    tax = (income - 10000) * 0.10
else:
    tax = 10000 * 0.10 + (income - 20000) * 0.20

print("Income Tax:", tax)
