def is_leap_year(year):
    """Determines whether a given year is a leap year or not."""
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

print(is_leap_year(1989))
print(is_leap_year(2400))

for year in range(2025, 2100):
    if is_leap_year(year):
        print(f"{year} is leap")
