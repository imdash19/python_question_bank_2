# Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.

def count_characters(text):
    frequency = {}

    for char in text.lower():
        if char != " ":
            frequency[char] = frequency.get(char, 0) + 1

    return frequency


text = input()

print(count_characters(text))
