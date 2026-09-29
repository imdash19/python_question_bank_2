# Perfect! Let me create the beginner-friendly version:

# 1. Problem Statement Description
# You need to create a program that calculates an electricity bill and applies a subsidy if applicable.
# The program should:

# Take the number of electricity units consumed as input
# Calculate the bill at a rate of 5 rupees per unit
# Apply a 20% subsidy if the units consumed are less than 100
# If units are 100 or more, no subsidy is applied

# Input Format:

# Single line: Number of units consumed (a number)

# Output Format:

# Print the final bill amount after applying subsidy (if applicable), rounded to 2 decimal places

class Student:
    def __init__(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks


class SportsMarks:
    def __init__(self, sports_marks):
        self.sports_marks = sports_marks

    def get_sports_marks(self):
        return self.sports_marks


class TotalMarks(Student, SportsMarks):
    def __init__(self, marks, sports_marks):
        Student.__init__(self, marks)
        SportsMarks.__init__(self, sports_marks)

    def calculate_total(self):
        total = self.get_marks() + self.get_sports_marks()

        print("Total:", total)

        if total >= 100:
            print("Pass")
        else:
            print("Fail")


marks = int(input())
sports_marks = int(input())

result = TotalMarks(marks, sports_marks)
result.calculate_total()
