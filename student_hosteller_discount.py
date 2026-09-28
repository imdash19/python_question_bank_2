# Create a base class Student with a method get_fee() to store/retrieve fee.
# Create One child classes:
# Hosteller → gets 20% discount

class Student:
    def __init__(self, fee):
        self.fee = fee

    def get_fee(self):
        return self.fee


class Hosteller(Student):
    def calculate_fee(self):
        fee = self.get_fee()
        discount = fee * 20 / 100
        return fee - discount


fee = float(input())

student = Hosteller(fee)

print(student.calculate_fee())
