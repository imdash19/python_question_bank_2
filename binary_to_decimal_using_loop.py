# Manually convert a binary string (e.g., "1101") into its decimal integer equivalent using a loop. Do not use int(binary, 2).

binary = input()

decimal = 0

for digit in binary:
    decimal = decimal * 2 + int(digit)

print("Decimal:", decimal)
