# Write a program to count the number of vowels in a string using recursion.
# The program should check the first character of the string.
# If it is a vowel, increment the count.
# Recursively call the function with the remaining string.
# Recursion stops when the string becomes empty.

def count_vowels(text):
    if text == "":
        return 0

    count = 1 if text[0].lower() in "aeiou" else 0

    return count + count_vowels(text[1:])


text = input()

print(count_vowels(text))
