# Create a class Units with method get_units(). 
# Create another class Subsidy with method apply_subsidy(). 
# Create a child class ElectricityBill that calculates bill and applies subsidy if units are below 100.

class Units:
    def get_units(self, units):
        return units


class Subsidy:
    def apply_subsidy(self, bill):
        if self.units < 100:
            return bill - (bill * 10 / 100)
        return bill


class ElectricityBill(Units, Subsidy):
    def calculate_bill(self, units):
        self.units = self.get_units(units)

        bill = self.units * 5
        bill = self.apply_subsidy(bill)

        return bill


units = int(input())

electricity_bill = ElectricityBill()

print(electricity_bill.calculate_bill(units))
