# Write a Python program to define a class Person.
# The class should have attributes: name and age.
# Define a method display() that prints the name and age.
# Create an object of the class.
# Call the display() method using the object
# Use self to access the attributes.
# Output should clearly show the person’s name and age.

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def display(self):
        return f'''Name: {self.name} 
Age: {self.age}'''


p= Person(input(), int(input()))
print(p.display())
