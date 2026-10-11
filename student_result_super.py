# Create Student parent class with marks attribute and child class use super to check pass or fail

# Parent Class Student stores the marks and validates the input.
# Child Class Result uses super().marks to reuse the parent attribute.
# Pass Criteria → marks ≥ 35.
# Prints "Pass" or "Fail" based on marks.

class Student:
    def __init__(self, marks):
        self.marks = marks

class Result(Student):
    def __init__(self, marks):
        super().__init__(marks)

    def check_result(self):
        if self.marks >= 35:
            print("Pass")
        else:
            print("Fail")

marks = int(input())

result = Result(marks)
result.check_result()
