# Write a Python program to define a class Person with attributes name and age.
# Accept the name and age of two persons from the user. 
# Create two objects person1 and person2 using these inputs.
# Display the name and age of both persons using object references. 
# Demonstrates object creation and attribute access.

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age

n1= input()
a1= int(input())
n2= input()
a2= int(input())

p1= Person(n1, a1)
p2= Person(n2, a2)

print(f'''Name: {p1.name}
Age: {p1.age}
Name: {p2.name}
Age: {p2.age}''')
