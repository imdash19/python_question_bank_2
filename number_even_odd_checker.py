# Create class Number with static method is_even that checks if input number is even or odd

class Number:
    @staticmethod
    def is_even(n):
        if n % 2 == 0:
            print('Even')
        else:
            print('Odd')

Number.is_even(int(input()))
