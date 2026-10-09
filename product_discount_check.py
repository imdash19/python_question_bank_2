# Create Product class with price attribute and print Discount Available if price >=1000

class Product:
    pass

p= Product()
p.price= int(input())

print('Discount Available' if p.price >= 1000 else 'No Discount')
