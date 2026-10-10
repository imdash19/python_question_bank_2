# Create a Student class with a constructor.
# The constructor should accept name and store it in a public attribute.
# Print the name in the format:

# Student Name: <name>

class Student:
    def __init__(self, name):
        self.name = name

name = input()
student = Student(name)

print(f"Student Name: {student.name}")
