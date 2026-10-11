# Create a Parent class with a name attribute.
# Create a Child class that uses super() to initialize the name from the parent class.
# Print the name in the format:
# Name: <name>

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

name = input()
child = Child(name)

print(f"Name: {child.name}")
