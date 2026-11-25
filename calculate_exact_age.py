# Create a function that asks for a user’s birthdate (YYYY-MM-DD) and calculates their exact age today in years, months, and days.

from datetime import date
import calendar

def calculate_age(birthdate):
    today = date.today()

    if birthdate > today:
        return "Invalid birthdate"

    total_months = (today.year - birthdate.year) * 12 + today.month - birthdate.month

    def add_months(start_date, months):
        month_index = start_date.month - 1 + months
        year = start_date.year + month_index // 12
        month = month_index % 12 + 1
        day = min(start_date.day, calendar.monthrange(year, month)[1])
        return date(year, month, day)

    anniversary = add_months(birthdate, total_months)

    if anniversary > today:
        total_months -= 1
        anniversary = add_months(birthdate, total_months)

    years, months = divmod(total_months, 12)
    days = (today - anniversary).days

    return years, months, days


birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = date.fromisoformat(birthdate)

age = calculate_age(birthdate)

if isinstance(age, tuple):
    years, months, days = age
    print(f"Your age is {years} years, {months} months, and {days} days.")
else:
    print(age)
