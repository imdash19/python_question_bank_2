# Write a Python program that takes any input from the user and finds out what type of data it is. When you use the input() function in Python, it always treats the data as text (string), no matter what you type. Your program should display the data type of this input.Input Format: Any value entered by the user (number, text, symbols, etc.)Output Format: The data type of the input, which will be <class 'str'>

s= input()
print(type(s))
