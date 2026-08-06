# Write a Python program that takes several age values entered by the user in a single line, separated by spaces. Your program should split these age values and store them in a set (a special collection that automatically removes duplicate values and keeps only unique items). Since sets are unordered and the output order may change every time, convert the set to a sorted list and then display it so the output is consistent.
# For example, if the user enters "20 25 20 30 25", your program should create a set that removes the duplicate values, convert it to a sorted list, and display it as ['20', '25', '30'] (only unique ages in order).
# Input Format:
# Multiple age values separated by spaces in a single line (e.g., "20 25 20 30")
# Output Format:
# A sorted list containing only the unique age values (e.g., ['20', '25', '30'])
# Note: Sets are unordered, so we convert the set to a sorted list to get consistent and ordered output.

age= list(set(input().split()))
age.sort()
print(sge)
