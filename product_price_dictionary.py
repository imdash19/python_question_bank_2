# Accept product names list and prices list create dictionary using zip

product= input().split()
price= list(map(int, input().split()))

product_price= dict(zip(product, price))
print(product_price)
