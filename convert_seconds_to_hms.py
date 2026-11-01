# Write a Python program to accept time in seconds.
# Convert it into hours, minutes, and seconds.
# Display the result in HH:MM:SS format.
# Ensure correct conversion logic.

total_seconds = int(input())
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
