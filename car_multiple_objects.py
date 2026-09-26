# Create a class Car with instance variable model. 
# Create two objects with different models and print both.

class Car:
    def __init__(self, model):
        self.model= model

c1= Car(input())
print(c1.model)
c2= Car(input())
print(input())
