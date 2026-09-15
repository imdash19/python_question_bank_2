# Write a Python program to create a class Employee having a class variable company_name = "TechCorp" 
# and instance variables name and employee_id. Accept employee details from the user. 
# Create multiple objects. Display employee name, employee ID, and company name.
# Verify that the company name remains the same for all objects while employee details differ. 
# Demonstrate how class variables are shared and instance variables are unique.

class Employee:
    company_name= 'TechCorp'
    def __init__(self, name, eid):
        self.name= name
        self.eid= eid

e= Employee(input(), int(input()))
print(f'''{e.name}
{e.eid}
{e.company_name}''')
