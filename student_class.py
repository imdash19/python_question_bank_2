# Write a Python program to define a class named Student.
# The class should store student name and roll number.
# Accept both values from the user through the console.
# Create an object using the input values. Access the attributes using the object reference. 
# Display the student details clearly. Use the self keyword to refer to instance variables.

class Student:
    def __init__(self, name, roll):
        self.name= name
        self.roll= roll

    def display(self):
        return f'''Name: {self.name}
        Roll: {self.roll}'''

s= Student(input(), int(input()))
print(s.display())
