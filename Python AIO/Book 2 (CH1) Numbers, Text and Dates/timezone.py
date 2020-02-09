# Get a datetime module and give it an alias
import datetime as dt

# Get the time from computer clock
here_now = dt.datetime.now()

# Get the UTC datetime right now
utc_now = dt.datetime.utcnow()

# Subtract to see difference
time_difference = (utc_now - here_now)

# Show results
print(f"My time    : {here_now:%I:%M:%p}")
print(f"UTC Time   : {utc_now:%I:%M:%p}")
print(f"Difference : {time_difference}")
