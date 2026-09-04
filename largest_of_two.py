# Define a function that returns the larger of two numbers entered 
# by the user. The function should handle the case when both numbers
# are equal. Use conditional statements inside the function to 
# compare the numbers.

def larger_number(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a


num1 = int(input())
num2 = int(input())

result = larger_number(num1, num2)

print(result)
