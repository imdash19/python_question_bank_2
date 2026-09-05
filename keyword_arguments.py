# Define a function that accepts name and age using 
# keyword arguments. Return a formatted string introducing
# the person. Test with arguments provided in any order.
# Helps understand keyword arguments.

def introduce(name, age):
    return f"My name is {name} and I am {age} years old."


result = introduce(age=22, name="Rahul")

print(result)
