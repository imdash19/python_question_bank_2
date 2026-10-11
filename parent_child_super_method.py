# Create Parent class with display method and Child class use super to call display method

class Parent:
    def display(self):
        print("Parent class method")

class Child(Parent):
    def display(self):
        super().display()

child = Child()
child.display()
