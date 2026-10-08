# Create a class Student with an instance method display_name that prints student name

class Student:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


name = input()

student = Student(name)
student.display_name()
