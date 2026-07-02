# Create a User class with a private attribute __password.
# Use a method to verify the password:
# Print "Access Granted" if input matches __password
# Print "Access Denied" otherwise

class User:
    def __init__(self, password):
        self.__password = password

    def verify_password(self, entered_password):
        if entered_password == self.__password:
            print("Access Granted")
        else:
            print("Access Denied")

password = input()
entered_password = input()

user = User(password)
user.verify_password(entered_password)
