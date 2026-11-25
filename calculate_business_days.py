# Create a function that takes a start date and an integer N, then calculates the date exactly N business days (Monday–Friday) in the future.

from datetime import datetime, timedelta

def add_business_days(start_date, n):
    current_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    count = 0

    while count < n:
        current_date += timedelta(days=1)

        if current_date.weekday() < 5:
            count += 1

    return current_date


start_date = input("Enter start date (YYYY-MM-DD): ")
n = int(input("Enter number of business days: "))

result = add_business_days(start_date, n)

print("Future Date:", result)
