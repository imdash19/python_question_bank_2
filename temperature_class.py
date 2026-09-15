# Write a Python program to define a class Temperature with attribute celsius.
# Add a method to_fahrenheit() that converts the Celsius value to Fahrenheit using 
# the formula F = (C × 9/5) + 32. Accept Celsius input from the user. 
# Create a Temperature object with the input value. Call the to_fahrenheit() method 
# and display the result. The program should handle negative Celsius values correctly.
# Round the Fahrenheit output to 2 decimal places.

class Temparature:
    def __init__(self, celsis):
        self.celsis= celsis

    def to_fahrenheit(self):
        return (self.celsis * (9/5)) + 32

t= Temparature(float(input()))
print(f'Fahrenheit: {t.to_fahrenheit()}')
