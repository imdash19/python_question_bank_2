# Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.

def is_palindrome(sentence):
    cleaned = ""

    for char in sentence.lower():
        if char.isalnum():
            cleaned += char

    return cleaned == cleaned[::-1]


sentence = input()

if is_palindrome(sentence):
    print("Palindrome")
else:
    print("Not Palindrome")
