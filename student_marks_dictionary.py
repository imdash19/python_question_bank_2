# Accept two lists student names and marks and create dictionary using zip then print it

names = input().split()
marks = list(map(int, input().split()))

student_dict = dict(zip(names, marks))

print(student_dict)
