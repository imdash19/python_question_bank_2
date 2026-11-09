# Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.

paragraph = input().lower()

words = paragraph.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
