# Create a class named Student. Inside the class define two public attributes name and marks. 
# Accept name and marks as input from the user. 
# Create an object of the Student class and directly access and print the values of name and marks using the object.

class Student:
    def __init__(self, name, mark):
        self.name= name
        self.mark= mark

s= Student(input(), int(input()))
print(s.name, s.mark)
