# Write a Python program to calculate the sum of natural numbers up to N.
# Accept an integer N from the user.
# Initialize a sum variable with value 0.
# Use a while loop to add numbers from 1 to N.
# Print the final calculated sum.

n= int(input())

sum= 0
i= 1

while i <= n:
    sum+= i
    i+= 1

print(sum)
