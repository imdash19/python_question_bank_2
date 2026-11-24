# Create a function that “inverts” a dictionary. Convert a dictionary of Author: [List of Books] into a dictionary of Book: Author.

def invert_dictionary(authors):
    books = {}

    for author, book_list in authors.items():
        for book in book_list:
            books[book] = author

    return books


authors = {
    "J.K. Rowling": ["Harry Potter", "Fantastic Beasts"],
    "George Orwell": ["1984", "Animal Farm"],
    "Dan Brown": ["The Da Vinci Code", "Inferno"]
}

print(invert_dictionary(authors))
