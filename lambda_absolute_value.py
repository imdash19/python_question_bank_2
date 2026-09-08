# Write an anonymous function to find the absolute value of a number. Input is a single integer.
# The program should return the absolute value. This demonstrates handling negative numbers 
# using anonymous functions.

absolute_number= lambda n: n if n > 0 else -n
print(absolute_number(int(input())))
