# Write a program to count how many times a character appears in a string using recursion.
# The program should compare the first character and increment count if it matches.
# Recursion continues on the remaining string.
# The output should be total count.

def count_character(text, character):
    if text == "":
        return 0

    count = 1 if text[0] == character else 0

    return count + count_character(text[1:], character)


text = input()
character = input()

print(count_character(text, character))
