# Write a function that accepts two numbers entered by the 
# user and returns their sum. The function should be reusable for 
# any pair of integers. The result must be returned and not printed 
# directly. The function can be called multiple times with different 
# inputs.

def add_numbers(a, b):
    return a + b


num1 = int(input())
num2 = int(input())

result = add_numbers(num1, num2)

print(result)
