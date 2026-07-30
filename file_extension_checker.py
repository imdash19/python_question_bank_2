# Write a Python program to read a filename.
# Check if it ends with .txt, .pdf, or .csv.
# If supported, print Supported.
# Otherwise, print Unsupported.

s= input()
print('Supported' if s[-4:] == '.txt' or s[-4:] == '.pdf' or s[-4:] == '.csv' else 'Unsupported')
