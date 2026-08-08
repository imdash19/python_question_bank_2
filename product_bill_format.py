# Write a Python program to accept product name, quantity, and price.
# Calculate the total cost.
# Use the .format() method to create a formatted bill.
# Print the bill details clearly.

product = input()
quantity = int(input())
price = float(input())

total = quantity * price

bill = "Product: {}\nQuantity: {}\nPrice: {:.2f}\nTotal: {:.2f}".format(
    product, quantity, price, total
)

print(bill)
