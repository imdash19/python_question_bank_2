# Create a class Student with attribute marks. 
# Overload the > operator using __gt__() to compare marks of two students and print who scored higher.

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


marks1 = int(input())
marks2 = int(input())

student1 = Student(marks1)
student2 = Student(marks2)

if student1 > student2:
    print("Student 1 scored higher")
elif student2 > student1:
    print("Student 2 scored higher")
else:
    print("Both students scored equal")
