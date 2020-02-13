# Need this modules for the dates.
import datetime as dt

# Create a list of dates, empty for starters
datelist = []

# Append dates one at time so code is easier to read.
datelist.append(dt.date(2020, 12, 31))
datelist.append(dt.date(2019, 1, 31))
datelist.append(dt.date(2018, 2, 28))
datelist.append(dt.date(2020, 1, 1))

# Sort the dates (earliest to latest) and show formatted.
datelist.sort()
for date in datelist:
	print(f"{date: %m/%d/%Y}")
