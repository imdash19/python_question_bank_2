# Write a program that uses a lambda function to calculate the square of a given number. Input is 
# a single integer provided through the console. The lambda function should return the square value. 
# This program explains how lambda functions replace small single-use functions. Test with positive, 
# negative, and zero values.

square= lambda n: n**2
print(square(int(input())))
