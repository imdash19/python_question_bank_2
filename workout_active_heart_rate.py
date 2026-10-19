# You are building a Smart Watch Heart Rate Monitor that tracks your heart rate at three different times during your workout session: before exercise (resting), during exercise (active), and after exercise (recovery).Here's how it works:

# Your smart watch records three heart rate readings during a workout
# First reading: Resting heart rate (before you start exercising)
# Second reading: Active heart rate (while you're exercising - this is the most important!)
# Third reading: Recovery heart rate (after you cool down)
# Fitness trainers focus on the active heart rate to measure workout intensity
# Example: If your readings are "72 145 95" (Resting: 72 bpm, Active: 145 bpm, Recovery: 95 bpm), the system should display your active workout heart rate: 145You need to create a program that:

# Takes three heart rate readings in a single line (separated by spaces)
# Stores them in a list (in order: resting, active, recovery)
# Accesses and displays only the second reading (active heart rate during workout)
# Input Format:

# Single line: Three heart rate values (integers) separated by spaces
# Output Format:

# Print only the second value (active workout heart rate)

heart_rates = list(map(int, input().split()))

print(heart_rates[1])
