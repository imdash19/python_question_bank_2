# A hotel stores room numbers from 1 to n. 
# For a maintenance report, it needs the square of each room number. 
# Take n as input and create a list of squares from 1 to n using list comprehension.

n= int(input())
lst= [i**2 for i in range(1, n+1)]
print(lst)
