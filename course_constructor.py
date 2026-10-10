# Create a class Course with non parameterized constructor that initializes course name and duration and prints them

class Course:
    def __init__(self):
        self.name = "Python"
        self.duration = "3 months"

    def display(self):
        print(self.name)
        print(self.duration)


course = Course()
course.display()
