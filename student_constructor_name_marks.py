# Create Student class with parameterized constructor to accept name and marks and print them

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

name = input()
marks = int(input())

student = Student(name, marks)

print("Name:", student.name)
print("Marks:", student.marks)
