# Import the datetime module give it an alias of dt
import datetime as dt

# Put today's date in today variable.
today = dt.date.today()

# Put another date in last_of_teens
last_of_teens = dt.date(2019, 12, 31)

# See what's in each variable.
print(today)
print(last_of_teens)

print(f"last_of_teens.month\t: {last_of_teens.month}")
print(f"last_of_teens.day\t: {last_of_teens.day}")
print(f"last_of_teens.year\t: {last_of_teens.year}")

# Using f-strings for formatting the dates
print(f"Formatting a date with f-string: {last_of_teens: %A, %B %d, %Y}")

right_now = dt.datetime.now()
print(right_now)

print("Calculating timespan...")
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day