# Write a Python program to find words in a string whose length is greater than a given number k. 
# The program should accept a string and value k. 
# Words are space-separated. Output should list valid words in order of appearance.

s= input().split()
k= int(input())

for v in s:
    if len(v) >= k:
        print(v, end= ' ')
