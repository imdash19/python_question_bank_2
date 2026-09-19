# Write a Python program to check whether a string contains any special character (non-alphanumeric). 
# The program should accept a string from the user. Only letters and digits are allowed. 
# If any other character is present, print TRUE; otherwise, print FALSE.

s= input()
print(not s.isalnum())
