# Reads multiple integers provided in a single line, separated by spaces. The program parses the input string into individual integer values and stores them in a list for further processing.

numbers = list(map(int, input().split()))

print(numbers)
