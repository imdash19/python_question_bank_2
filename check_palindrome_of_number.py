# Write a program to check if a given number is a palindrome. A palindrome number is a number that remains the same when its digits are reversed (e.g., 121, 343).

n= int(input())
on= n
nn= 0

while n:
  nn= (nn * 10) + (n % 10)
  n//= 10

print('Pallindrome' if on == nn else 'Not a Pallindrome')
