# Write a function to remove characters from a string starting from index 0 up to n and return a new string.

def remove_characters(text, n):
    return text[n:]


text = input()
n = int(input())

print(remove_characters(text, n))
