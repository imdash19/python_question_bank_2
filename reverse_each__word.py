# Given a sentence, reverse each individual word within the string while maintaining the original word order.

sentence = input()

words = sentence.split()

reversed_words = []

for word in words:
    reverse = ""

    for char in word:
        reverse = char + reverse

    reversed_words.append(reverse)

print(" ".join(reversed_words))
