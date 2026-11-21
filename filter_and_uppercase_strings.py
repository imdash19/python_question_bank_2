# Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.

words = input().split()

result = [word.upper() for word in words if len(word) >= 4]

print(result)
