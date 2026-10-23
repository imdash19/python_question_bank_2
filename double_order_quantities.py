# An order system doubles quantities during bulk sales. 
# Take two quantities as input and create a list with doubled values using list comprehension.

lst= list(map(int, input().split()))
nlst= [v*2 for v in lst]
print(nlst)
