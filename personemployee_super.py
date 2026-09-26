# Create a parent class User with a method greet() that prints "Welcome User".
# Create a child class Customer. Inside the child class, create a method show_greeting() and call the parent class method greet() using super().

class User:
    def greet(self):
        return 'Welcome User'

class Customer(User):
    def show_greetings(self):
        return super().greet()

print(Customer().show_greetings())
