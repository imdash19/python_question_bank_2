# You are creating a Daily Temperature Dashboard for a weather app that helps people plan their outdoor activities. The app tracks temperature at three key times: morning (when people wake up), noon (hottest part of the day), and evening (when people return home).Here's how it works:

# The weather station records three temperature readings throughout the day
# First reading: Morning temperature (around 8 AM)
# Second reading: Noon temperature (around 12 PM - typically the hottest!)
# Third reading: Evening temperature (around 6 PM)
# The noon temperature is crucial for people planning lunch breaks, outdoor sports, or picnics
# Example: If the daily readings are "28 35 30" (Morning: 28°C, Noon: 35°C, Evening: 30°C), the system should display the peak noon temperature: 35You need to create a program that:

# Takes three temperature readings in a single line (separated by spaces)
# Stores them in a list (in order: morning, noon, evening)
# Accesses and displays only the second reading (noon temperature - the peak heat)
# Input Format:

# Single line: Three temperature values (integers) separated by spaces
# Output Format:

# Print only the second value (noon temperature)

temperatures = list(map(int, input().split()))

print(temperatures[1])
