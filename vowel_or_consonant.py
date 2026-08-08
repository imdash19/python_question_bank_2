# Write a Python program to take a single character as input.
# Compare the character with vowels (a, e, i, o, u).
# Consider both uppercase and lowercase letters.
# Print Vowel if it matches, otherwise print Consonant.

s= input()
print('Vowel' if s.lower() in 'aeiou' else 'Consonant')
