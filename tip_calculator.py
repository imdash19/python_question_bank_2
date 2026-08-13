# Write a Python program to calculate tip amount based on bill value and service quality.
# Rules:
# If bill > ₹2000 → 10% tip
# If bill > ₹5000 → 15% tip
# If service is "Excellent" → Add extra 5% tip

# Input Format:
# Integer: bill_amount
# String: service_quality (e.g., "Good", "Excellent")

# Output Format:
# Print: "Tip: ₹amount"

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
