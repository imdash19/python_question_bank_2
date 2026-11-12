# Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method.

text = input()

words = text.split()
result = []

for word in words:
    result.append(word[0].upper() + word[1:].lower())

print(" ".join(result))
