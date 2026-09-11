# You need to write a program that generates numbers from 1 to N using a generator function.
# A generator is a special function that produces values one by one instead of creating all values at once. Think of it like a ticket dispenser - it gives you one ticket at a time when you need it, rather than printing all tickets together.
# Your task is simple:

# Take a number N from the user
# Create a generator function that yields numbers from 1 to N
# Print each number on a new line

# Input Format: One integer N
# Output Format: Numbers from 1 to N, each on a separate line

def generator_numbers(n):
    for i in range(1, n+1):
        yield i

n= int(input())
for num in generator_numbers(n):
    print(num)
