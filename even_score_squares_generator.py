# A game system stores scores from 1 to n. It needs squares of only even scores. 
# Take n as input and generate the list.

n= int(input())
ticket= [val ** 2 for val in range(1, n+1) if val % 2 == 0]
print(ticket)
