# Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.

s= input()
consonant= 0
vowel= 0

for v in s:
  if v.lower() in 'aeiou':
    vowel+= 1
  elif v.lower() in 'bcdefghjklmnpqrstvwxyz':
    consonant+= 1

print(f'Vowels= {v}, Consonant: {c}')
