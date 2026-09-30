# Create a parent class Employee with method show_role() that prints Employee. 
# Create a child class Manager that overrides show_role() to print Manager.

class Employee:
    def show_role(self):
        print('Manager')

class Manager(Employee):
    def show_role(self):
        print('Manager')

Manager().show_role()
