# Write a function that calculates the exact number of days, hours, and minutes remaining until the upcoming New Year’s Day.

from datetime import datetime

def time_until_new_year():
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)

    remaining = new_year - now

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes = remainder // 60

    return days, hours, minutes


days, hours, minutes = time_until_new_year()

print(f"Time remaining until New Year: {days} days, {hours} hours, {minutes} minutes")
