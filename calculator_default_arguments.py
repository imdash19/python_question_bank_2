# Create a class Calculator with a method add(). The method should add two or three numbers depending on the input. Use default arguments to handle the case when only two numbers are provided.
# If two numbers are passed, return their sum.
# If three numbers are passed, return the sum of all three numbers.

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


numbers = list(map(int, input().split()))

calculator = Calculator()

if len(numbers) == 2:
    print(calculator.add(numbers[0], numbers[1]))
elif len(numbers) == 3:
    print(calculator.add(numbers[0], numbers[1], numbers[2]))
