# Write a function that greets a user. The function should have a
# default name value "Guest". Return the greeting string.
# Test with and without providing a name. Helps understand 
# default argument values.

def greet(name="Guest"):
    return "Hello, " + name + "!"


print(greet())
print(greet("Rahul"))
