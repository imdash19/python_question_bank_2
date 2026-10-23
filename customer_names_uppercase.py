# A system stores customer names in lowercase. 
# Take two names as input and convert them to uppercase using list comprehension.

lst= input().split()
nlst= [v.upper() for v in lst]
print(nlst)
