import calendar
# Interoperable libraries
import datetime
import time

print(calendar.weekheader(3))

# Prints index of weekday
print(calendar.firstweekday())

# Prints year, month, spacing
print(calendar.month(2020, 5, 2, 2))

# Prints array of dates
print(calendar.monthcalendar(2020, 5))

print(calendar.calendar(2020))

# for i in range(1, 12):
#    print(calendar.monthcalendar(2020, i))

day_of_the_week = calendar.weekday(2020, 6, 6)
print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000, 2021)
print(how_many_leap_days)
