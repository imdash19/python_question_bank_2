# Write a Python program to calculate car rental charges based on car type and day of the week.
# Rates:
# "Sedan" → ₹1000/day
# "SUV" → ₹1500/day
# On weekends ("Saturday" or "Sunday"), add 20% surge to the base cost

# Input Format:
# String: car_type (either "Sedan" or "SUV")
# String: day (e.g., "Monday", "Sunday")

# Output Format:
# Print: "Cost: ₹amount"

bill_amount = int(input())
service_quality = input()

if bill_amount > 5000:
    tip_rate = 0.15
elif bill_amount > 2000:
    tip_rate = 0.10
else:
    tip_rate = 0.0

if service_quality == "Excellent":
    tip_rate += 0.05

tip_amount = bill_amount * tip_rate

print("Tip: ₹", int(tip_amount))
