# Write a Python program to check if the elevator is safe based on the number of people and total weight.
# Rules:
# Max people: 8
# Max weight: 600 kg
# If either limit is exceeded, print "Overload"
# Otherwise, print "Safe"

# Input Format:
# Integer: people
# Integer: weight

# Output Format:
# Print: "Safe" or "Overload"

people = int(input())
weight = int(input())

if people > 8 or weight > 600:
    print("Overload")
else:
    print("Safe")
