# Write a Python program to create a class Book with class variable library_name = "Central Library" 
# and instance variables title and author. Accept book details from the user. 
# Create book objects and display book information along with library name.
# Verify that all books belong to the same library while book details differ.

class Book:
    library_name = "Central Library" 
    def __init__(self, title, author):
        self.title= title
        self.author= author

b= Book(input(), input())
print(f'''{b.title}
{b.author}
{b.library_name}
''')
