# Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

num= int(input())

num1= num
num2= 0

while num:
  num2= (num2*10) + num%10
  num//= 10

print('Pallindrum' if num1 == num2 else 'Not Pallindrum')
