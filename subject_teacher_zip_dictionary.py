# Accept subjects list and teachers list create dictionary using zip

subjects = input().split()
teachers = input().split()

subject_teacher = dict(zip(subjects, teachers))

print(subject_teacher)
