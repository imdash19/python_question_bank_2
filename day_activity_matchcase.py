# Write a Python program that suggests an activity based on the day of the week.
# The program should take a day name as input (like Monday, Tuesday, etc.).
# Use the match-case statement to match the day and print the planned activity:

# Monday → Go for a run

# Tuesday → Attend a cooking class

# Wednesday → Work on a personal project

# Thursday → Watch a movie

# Friday → Hang out with friends

# Saturday → Go shopping

# Sunday → Relax at home

# If the input does not match any day, print:

# Invalid day input.

day = input().lower()

match day:
    case "monday":
        print("Go for a run")
    case "tuesday":
        print("Attend a cooking class")
    case "wednesday":
        print("Work on a personal project")
    case "thursday":
        print("Watch a movie")
    case "friday":
        print("Hang out with friends")
    case "saturday":
        print("Go shopping")
    case "sunday":
        print("Relax at home")
    case _:
        print("Invalid day input.")
