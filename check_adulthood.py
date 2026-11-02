# Write a Python program to read age and country (India or USA).
# Check adulthood based on the given country.
# In India, adult age is 18; in the USA, it is 21.
# Print Adult or Not Adult accordingly.

age, country= int(input()), input()

if age >= 18 and country.lower() == 'india':
    print('Adult')
elif age >= 21 and country.lower() == 'usa':
    print('Adult')
else:
    print('Not Adult')
