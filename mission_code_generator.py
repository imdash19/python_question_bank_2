# Beginner-Friendly Python Question

# 1. Problem Statement Description
# You are creating a Secret Agent Mission Code Generator for a spy agency. Every mission gets a unique code number, and for security purposes, all mission codes must be exactly the same length with leading zeros.
# Here's how it works:

# Each mission is assigned a unique mission number (like 7, 99, 1543)
# All mission codes must have the exact same number of digits for the security system to work
# If a mission number has fewer digits than required, zeros are added at the beginning
# This ensures all agents see uniform, professional-looking mission codes

# Example 1: Mission number = 7, Code length = 5
# Output: "Mission Code: 00007"
# Example 2: Mission number = 238, Code length = 6
# Output: "Mission Code: 000238"
# You need to create a program that:

# Takes a mission number as input
# Takes the required code length (total digits) as input
# Generates and displays the complete mission code with leading zeros using modern f-string syntax

# Input Format:

# First line: Mission number (integer)
# Second line: Required code length (integer)

# Output Format:

# Print "Mission Code: " followed by the zero-padded mission number

mission_number = int(input())
code_length = int(input())

mission_code = f"{mission_number:0{code_length}d}"

print(f"Mission Code: {mission_code}")
