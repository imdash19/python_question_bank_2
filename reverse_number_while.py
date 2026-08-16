# Write a Python program to reverse the digits of a number.
# Accept an integer input from the user.
# Use a while loop to extract digits one by one.
# Build the reversed number using arithmetic operations.
# Print the reversed number as output.

n= int(input())
new= 0

while n != 0:
    new= (new*10) + (n%10)
    n//= 10
print(new)
