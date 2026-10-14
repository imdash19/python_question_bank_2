# Accept course names list and durations list create dictionary using zip

courses = input().split()
durations = input().split()

course_dict = dict(zip(courses, durations))

print(course_dict)
