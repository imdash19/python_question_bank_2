# Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’.

def rotate_list(lst, n, direction):
    if not lst:
        return lst

    n = n % len(lst)

    if direction.lower() == "left":
        return lst[n:] + lst[:n]
    elif direction.lower() == "right":
        return lst[-n:] + lst[:-n] if n != 0 else lst
    else:
        return "Invalid direction"


numbers = list(map(int, input().split()))
n = int(input())
direction = input()

print(rotate_list(numbers, n, direction))
