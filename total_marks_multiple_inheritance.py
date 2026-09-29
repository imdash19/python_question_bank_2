# Create a base class Student with method get_marks(). 
# Create class SportsMarks with method get_sports_marks(). 
# Create a class TotalMarks inheriting both to calculate total and print Pass if total >= 100 else Fail.

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
