# Write a program to calculate grades for students based on marks.
# The program should accept space-separated marks from the user.
# Grade conditions must be defined using conditional expressions.
# The program should use map() with lambda.
# Each mark should be converted into a grade.
# The output should be a list of grades.
# Grade Criteria

# Marks Range Grade
# 90 – 100 A
# 75 – 89 B
# 60 – 74 C
# 40 – 59 D
# Below 40 F

marks = list(map(int, input().split()))

grades = list(map(
    lambda m: "A" if m >= 90 else
              "B" if m >= 75 else
              "C" if m >= 60 else
              "D" if m >= 40 else
              "F",
    marks
))

print(grades)
