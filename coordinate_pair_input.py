# Reads two integers representing x and y coordinates from a single line of input. The program parses and stores them as a coordinate pair for geometric or mapping applications.

x, y= map(int, input().split())
print(f'({x}, {y})')
