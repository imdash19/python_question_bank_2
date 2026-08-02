# Write a Python program to create a list of strings.
# Sort the list first by the length of each string.
# If strings have the same length, sort them alphabetically.
# Use Python’s sorting functions to arrange the list.
# Print the sorted list.

words = input().split()

words.sort(key=lambda word: (len(word), word))

print(words)
