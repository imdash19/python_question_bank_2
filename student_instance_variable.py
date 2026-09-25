# Create a class Student. Inside the constructor define an instance variable name. 
# Accept the name from the user. Create an object and print the name using the object reference.

class Student:
    def __init__(self, name):
        self.name= name

s= Student(input())
print(s.name)
