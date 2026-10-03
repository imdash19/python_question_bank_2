# Reads a phone number as a sequence of digits and converts it to an integer. The program validates that the input contains exactly 10 digits (or other specified length).

ph= input()
if len(ph) == 10 and int(ph):
    print(int(ph))
else:
    print('Invalid')
