# Write a Python program to read a sentence.
# Check whether it contains spam, hack, or fake.
# If any word is found, print Blocked.
# Otherwise, print Allowed.

sen= input().split()
sen= [val.lower() for val in sen]
print('Allowed' if 'spam' not in sen and 'hack' not in sen and 'fake' not in sen else 'Blocked')
