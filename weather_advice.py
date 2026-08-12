# Write a Python program to give weather advice based on the temperature and raining status.
# Rules:
# Temperature > 30 → "Hot"
# Temperature < 10 → "Cold"
# Otherwise → "Moderate"
# If raining is True, add "Carry umbrella." to the output
# Input Format:
# Integer: temperature
# Boolean: raining
# Print the weather description and, if applicable, "Carry umbrella."

temperature = int(input())
raining = input() == "True"

if temperature > 30:
    weather = "Hot"
elif temperature < 10:
    weather = "Cold"
else:
    weather = "Moderate"

print(weather)

if raining:
    print("Carry umbrella.")
