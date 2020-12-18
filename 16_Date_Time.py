# Use Maya for an easier datetime module

import datetime
import pytz

# datetime.date = (Y, M, D)
# datetime.time = (h, m, s, ms)
# datetime.datetime = (Y, M, D, h, m, s, ms)

# Adds 10 days
today = datetime.date.today()
print(today)
day_delta = datetime.timedelta(days=10)
print(today + day_delta)

# Adds 10 hours
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now())
print(datetime.datetime.now() + hour_delta)
print()

# These are objects NOT strings
birthday = datetime.date(1999, 5, 1)
print(birthday)

# Days since birth
since_birth = today - birthday
days_since_birth = since_birth.days
print(since_birth)
print(days_since_birth)

# Years since birth
years_since_birth = today.year - birthday.year
print(years_since_birth)
print()

# Monday = 0, Sunday = 6
print(today.weekday())
print()

# Timezones
datetime_today = datetime.datetime.now(tz=pytz.utc)
datetime_pacific = datetime_today.astimezone(pytz.timezone("US/Pacific"))
print(datetime_today)
print(datetime_pacific)

# Prints all timezones
"""
for tz in pytz.all_timezones:
    print(tz)
"""
print()

# Formatting (B = Month, d = Day, Y= Year)
datetime_gb = datetime_today.astimezone(pytz.timezone("GB"))
print(datetime_gb)
gb_formatted = datetime_gb.strftime("%B %d, %Y")
print(gb_formatted)

# Parsing
gb_parsed = datetime.datetime.strptime(gb_formatted, "%B %d, %Y")
print(gb_parsed)
