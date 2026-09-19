# Write a Python program to print all words of even length from a given string. 
# The program should accept a sentence from the user. Each word is separated by spaces. 
# Only words with even number of characters should be printed. 
# Output words are space-separated. Case should remain as in input.

s= input().split()

for v in s:
    if len(v)%2==0:
        print(v, end= ' ')
