# You are organizing a Marathon Race Event and need to generate race bib numbers for all participants. Race bibs are the number tags that runners wear during the race, and they must all have the same format for easy identification.Here's how it works:

# Each runner is assigned a unique participant number (like 5, 127, 2048)
# All race bib numbers must have the same total number of digits for consistency
# If a participant number has fewer digits than required, zeros are added at the beginning
# This creates a professional, uniform look for all race bibs and makes timing systems work properly
# Example 1: Participant number = 25, Bib digits = 5
# Output: "Race Bib: 00025"Example 2: Participant number = 789, Bib digits = 6
# Output: "Race Bib: 000789"You need to create a program that:

# Takes a participant number as input
# Takes the required bib number length (total digits) as input
# Generates and displays the race bib number with leading zeros using the traditional %-formatting method
# Input Format:

# First line: Participant number (integer)
# Second line: Required bib number length (integer)
# Output Format:

# Print "Race Bib: " followed by the zero-padded participant number

participant_number = int(input())
bib_length = int(input())

race_bib = ("%0" + str(bib_length) + "d") % participant_number

print("Race Bib:", race_bib)
