import calendar

assert(calendar.weekday(1900, 1, 1) == calendar.MONDAY)

sundays = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if calendar.weekday(year, month, 1) == calendar.SUNDAY:
            sundays += 1

print sundays
