# Create a Book class with attributes title and price then create an object and print them

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price


title = input()
price = float(input())

book = Book(title, price)

print(book.title)
print(book.price)
