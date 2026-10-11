# Create a Result class with a public attribute marks.
# Use a constructor to initialize the marks.
# Print "Pass" if marks ≥ 40, else "Fail".

class Result:
    def __init__(self, marks):
        self.marks = marks

marks = int(input())
result = Result(marks)

if result.marks >= 40:
    print("Pass")
else:
    print("Fail")
