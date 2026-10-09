# Create a class Marks with instance method add_marks that adds two inputs and prints result

class Mark:
    def add_marks(self, a, b):
        return f'Total: {a+b}'

a, b= input().split()
print(Mark().add_marks(int(a), int(b)))
