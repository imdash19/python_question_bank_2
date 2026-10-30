# A school system stores each student as a record containing name and marks. 
# Take a student name and marks as input and store them as a nested tuple.
# Print the nested structure.

name = input()
marks = int(input())

student = ((name, marks),)

print(student)
