# Write a Python program to define a class named Movie.
# The class should contain attributes name, director, and rating.
# The program must accept movie details from the user through console input. 
# Use a constructor to initialize all attributes with the entered values. 
# Create an object of the Movie class using the user-provided data. 
# Access each attribute using dot notation. 
# Display all movie details clearly in the output.

class Movie:
    def __init__(self, name, director, rating):
        self.name = name
        self.director = director
        self.rating = rating


name = input()
director = input()
rating = float(input())

movie = Movie(name, director, rating)

print("Movie Name:", movie.name)
print("Director:", movie.director)
print("Rating:", movie.rating)
