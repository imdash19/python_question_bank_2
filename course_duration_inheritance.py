# Write a program to demonstrate inheritance using a parent and child class to classify a course based on its duration.

# Description
# Create a parent class Course with a duration attribute.
# Create a child class that inherits from the Course class.
# Use the super() method to pass the duration value to the parent class constructor.
# Based on the course duration, classify the course as long or short.

# Duration Conditions
# If duration is 6 months more, print “Long Course”
# If duration is less than 6 months, print “Short Course”

class Course:
    def __init__(self, duration):
        self.duration= duration

class OnlineCourse(Course):
    def __init__(self, duration):
        super().__init__(duration)

    def check_status(self):
        if self.duration > 6:
            return 'Long Course'

        else:
            return 'Short Course'

o= OnlineCourse(int(input()))
print(o.check_status())
