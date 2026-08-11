# Write a Python program to take the name of a day as input.
# Use ELIF conditions to check whether the day is a weekday or weekend.
# Consider Saturday and Sunday as weekends.
# Print Weekend or Weekday based on the input

day = input().lower()

if day == "saturday":
    print("Weekend")
elif day == "sunday":
    print("Weekend")
else:
    print("Weekday")
