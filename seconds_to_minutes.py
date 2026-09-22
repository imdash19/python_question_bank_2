# Write a program to convert seconds into minutes. 
# The program should accept a space-separated list of seconds from the user. 
# Each value should be converted into minutes. 
# The conversion must be done using division. 
# Python’s map() function should be used.
# The output should be a list of float values.

seconds = list(map(float, input().split()))

minutes = list(map(lambda x: x / 60, seconds))

print(minutes)
