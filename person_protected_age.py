# Create a Person class with a protected attribute _age.
# Access the protected attribute using a method inside the class.
# Print the age in the format:

# Age: <age>

class Person:
    def __init__(self, age):
        self._age = age

    def display_age(self):
        print(f"Age: {self._age}")


age = int(input())
person = Person(age)
person.display_age()
