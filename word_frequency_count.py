# Write a program to count the frequency of each word in a given string.

text = input().lower()

words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)
