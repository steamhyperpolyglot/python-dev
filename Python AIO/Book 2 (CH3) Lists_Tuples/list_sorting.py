# Need this modules for the dates.
import datetime as dt

# Create a list of strings.
names = ["Zara", "Lupe", "Alberto", "Jake", "Tyler"]
# Create a list of numbers
numbers = [14, 0, 56, -4, 99, 56, 11.26]

# Sort the names list
names.sort()
# Sort the numbers list
numbers.sort()

# Show the results
print("Sorting in ascending order...")
print(names)
print(numbers)

# Sort strings in reverse order
names.sort(reverse=True)
print(names)
print()     # This just adds a blank line to the output

# Sort numbers in reverse order (largest to smallest and show.
numbers.sort(reverse=True)
print(numbers)
print()

# Create a list of dates, empty for starters
datelist = []

# Append dates one at time so code is easier to read.
datelist.append(dt.date(2020, 12, 31))
datelist.append(dt.date(2019, 1, 31))
datelist.append(dt.date(2018, 2, 28))
datelist.append(dt.date(2020, 1, 1))

# Sort the dates in reversed order
datelist.sort(reverse=True)
for date in datelist:
	print(f"{date: %m/%d/%Y}")
