# Create a Mobile class with a constructor.
# The constructor should accept battery percentage and print:

# "Charge Phone" if battery < 20
# "Battery OK" if battery ≥ 20

class Mobile:
    def __init__(self, battery):
        self.battery= battery

m= Mobile(int(input()))

if m.battery >= 20:
    print('Battery OK')
else:
    print('Charge Phone')
