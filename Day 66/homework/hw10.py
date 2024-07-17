from datetime import date

def time_for_milk_and_cookies(dt):
    return dt.month == 12 and dt.day == 24

print(time_for_milk_and_cookies(date(2050, 12, 24)))
print(time_for_milk_and_cookies(date(2024, 12, 21)))