# A ticketing system generates odd-numbered tickets only. 
# Take n as input and generate a list of odd numbers up to n.

n= int(input())
tickets= [val for val in range(1, n+1) if val % 2 != 0]
print(tickets)
