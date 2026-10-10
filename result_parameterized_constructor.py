# Create a Result class with a parameterized constructor.
# The constructor should accept marks and print:

# "Pass" if marks ≥ 40
# "Fail" if marks < 40

class Result:
    def __init__(self, marks):
        if marks >= 40:
            print("Pass")
        else:
            print("Fail")


marks = int(input())
result = Result(marks)
