# Write a Python program to accept weight in kilograms.
# Accept height in meters.
# Calculate BMI using BMI = weight / height².
# Display the BMI value with 4 decimal places
# Hint: Use round() function

weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

print(f"{round(bmi, 4):.4f}")
