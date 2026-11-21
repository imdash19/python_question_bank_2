# Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).

def count_characters(text):
    frequency = {}

    for char in text.lower():
        if char != " ":
            frequency[char] = frequency.get(char, 0) + 1

    return frequency


text = input()

print(count_characters(text))
