# Write a function that checks if a number entered by the user is 
# even or odd. The function should take a single integer and return 
# 'Even' or 'Odd'. It should work with positive, negative numbers, 
# and zero. Use the modulo operator (%) to determine divisibility.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input())

result = check_even_odd(num)

print(result)
