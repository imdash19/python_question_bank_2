# Accept two lists with same values and print a is b

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(a is b)
