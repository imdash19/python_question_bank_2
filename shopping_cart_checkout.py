# Create base class Cart with method get_price(). 
# Create child class TaxCalculator that adds 10 percent tax. 
# Create another child class Checkout that applies 5 percent discount if total exceeds 1000.

class Cart:
    def get_price(self, price):
        self.price = price

class TaxCalculator(Cart):
    def add_tax(self):
        self.amount = self.price + (self.price * 0.10)

class Checkout(TaxCalculator):
    def discount(self):
        if self.price > 1000:
            self.amount = self.price - (self.price * 0.05)
        else:
            self.add_tax()
        return int(self.amount)

c = Checkout()
c.get_price(int(input()))
print(c.discount())
