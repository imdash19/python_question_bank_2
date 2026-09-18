# Write a Python program to check whether a given string is a palindrome. 
# The program should accept a string from the user. 
# A palindrome string reads the same forward and backward. 
# Case differences should be ignored. Spaces should be ignored while checking. 
# The program should reverse the string logically. 
# The result should clearly indicate palindrome or not.

text = input()

text = text.replace(" ", "").lower()

reverse_text = text[::-1]

if text == reverse_text:
    print("Palindrome")
else:
    print("Not Palindrome")
