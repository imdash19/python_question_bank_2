# Write a program to display all prime numbers within a range (e.g., 25 to 50). A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

start = int(input())
end = int(input())

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)
