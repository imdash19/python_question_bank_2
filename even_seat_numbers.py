# A theater wants to display only even seat numbers up to n. 
# Take n as input and generate a list of even numbers up to n using list comprehension.

n= int(input())
lst= [i for i in range(1, n+1) if i % 2 == 0]
print(lst)
