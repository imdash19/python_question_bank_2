# Create a Student class with attributes name and age then create an object and print the values

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


name = input()
age = int(input())

student = Student(name, age)

print(student.name)
print(student.age)
