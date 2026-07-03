# Write a program to demonstrate the use of instance variables in Python to check if a student has passed based on marks.

# Description
# Create a Student class with a constructor that accepts marks as an instance variable.
# Use the instance variable to determine the result:
# If marks >= 40, print “Pass”
# Else, print “Fail

class Student:
    def __init__(self, mark):
        self.mark= mark

    def check_status(self):
        if self.mark >= 40:
            return 'Pass'

        else:
            return 'Fail'

s= Student(int(input()))
print(s.check_status())
