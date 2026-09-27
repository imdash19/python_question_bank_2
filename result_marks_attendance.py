# Create a class Marks with method get_marks(). 
# Create another class Attendance with method get_attendance(). 
# Create a child class Result that calculates pass or fail based on marks >= 40 and attendance >= 75.

class Marks:
    def get_marks(self, marks):
        return marks


class Attendance:
    def get_attendance(self, attendance):
        return attendance


class Result(Marks, Attendance):
    def check_result(self, marks, attendance):
        marks = self.get_marks(marks)
        attendance = self.get_attendance(attendance)

        if marks >= 40 and attendance >= 75:
            print("Pass")
        else:
            print("Fail")


marks = int(input())
attendance = int(input())

result = Result()
result.check_result(marks, attendance)
