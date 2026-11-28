# You have two separate lists: one of student names and one of their exam scores. Use zip() to combine them into a dictionary, then use enumerate() to print a ranked list (1st, 2nd, 3rd…).

names = input("Enter student names: ").split()
scores = list(map(int, input("Enter exam scores: ").split()))

if len(names) != len(scores):
    print("Error: Number of names and scores must be equal.")
else:
    students = dict(zip(names, scores))

    ranked_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

    for rank, (name, score) in enumerate(ranked_students, start=1):
        suffix = "th" if 10 <= rank % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(rank % 10, "th")
        print(f"{rank}{suffix} - {name}: {score}")
