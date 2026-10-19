# Beginner-Friendly Python Question

# 1. Problem Statement Description
# You are organizing a Class Presentation Schedule where students need to present their projects one by one. The teacher has prepared a list of students in the order they will present, and you need to announce who presents first.
# Here's how it works:

# The teacher has a list of students who will give presentations
# Students are listed in the exact order they will present
# Your job is to identify and announce the first student who will present
# This helps the first student prepare and be ready when class starts

# Example: If the presentation order is "Ravi Anu Sam", the first presenter is "Ravi", so the system displays: Ravi
# You need to create a program that:

# Takes multiple student names in a single line (separated by spaces)
# Stores them in a list (in presentation order)
# Accesses and displays only the first student name (first presenter)

# Input Format:

# Single line: Multiple student names separated by spaces

# Output Format:

# Print only the first student name (first presenter)


students = input().split()

print(students[0])
