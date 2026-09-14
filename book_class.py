# Write a Python program to define a class named Book.
# The class should contain three attributes: title, author, and pages.
# The program must accept book information from the user through console input.
# Use a constructor to initialize all the attributes with the given values.
# Create an object of the Book class using the user-entered details.
# Access each attribute using dot (.) notation.
# Display all the book details clearly in the output.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


title = input()
author = input()
pages = int(input())

book = Book(title, author, pages)

print("Title:", book.title)
print("Author:", book.author)
print("Pages:", book.pages)
