# A class register stores each student as (name, marks). 
# Take two student records as input and store them in a nested tuple. 
# Print the structure.

name, marks= input().split()
name1, marks1= input().split()
t= ((name, marks), (name1, marks1))
print(t)
