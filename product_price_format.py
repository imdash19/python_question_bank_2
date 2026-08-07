# Write a Python program that takes the name of a product and its price from the user. Then display the information in a formatted way using the old-style % formatting method. The output should show the product name and its price with exactly 2 decimal places in a dollar format.
# For example, if the user enters "Book" and "99", your program should display "The price of Book is $99.00".
# Input Format:
# Two separate lines:

# First line: Product name (text)
# Second line: Price (number)

# Output Format:
# A formatted message showing: "The price of [product] is $[price]" where price has exactly 2 decimal places

product = input()
price = float(input())

print("The price of %s is $%.2f" % (product, price))
