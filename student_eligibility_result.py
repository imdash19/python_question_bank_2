# Create base class Student with method get_attendance(). 
# Create child class Eligibility that checks eligibility using if condition. 
# Create another child class Result that prints Eligible or Not Eligible.

class Student:
    def get_attendance(self, attendance):
        self.attendance = attendance


class Eligibility(Student):
    def check_eligibility(self):
        if self.attendance >= 75:
            self.status = "Eligible"
        else:
            self.status = "Not Eligible"


class Result(Eligibility):
    def print_result(self):
        print(self.status)


r = Result()
r.get_attendance(int(input()))
r.check_eligibility()
r.print_result()
