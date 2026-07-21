# Design a program using Multilevel Inheritance:
# Create base class Meter with method get_units(). 
# Create child class BillCalculator that calculates bill amount. 
# Create another child class FinalBill that applies 5 percent discount if units are below 100.

class Meter:
    def get_units(self, units):
        self.units = units


class BillCalculator(Meter):
    def calculate_bill(self):
        if self.units < 100:
            self.bill = self.units * 4
        else:
            self.bill = self.units * 5


class FinalBill(BillCalculator):
    def apply_discount(self):
        if self.units < 100:
            self.bill = self.bill - (self.bill * 0.05)
        return int(self.bill)


m = FinalBill()
m.get_units(int(input()))
m.calculate_bill()
print(m.apply_discount())
