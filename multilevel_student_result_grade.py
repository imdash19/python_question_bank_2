# Design a program using Multilevel Inheritance.

# Create a base class Student with method get_marks().
# Create a child class Result that calculates total and percentage.
# Create another child class Grade that assigns grade using if-else based on percentage.

class Student:
    def __init__(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks


class Result(Student):
    def calculate_result(self):
        total = sum(self.get_marks())
        percentage = total / len(self.get_marks())
        return total, percentage


class Grade(Result):
    def assign_grade(self):
        total, percentage = self.calculate_result()

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        return total, percentage, grade


marks = list(map(int, input().split()))

student = Grade(marks)

total, percentage, grade = student.assign_grade()

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
