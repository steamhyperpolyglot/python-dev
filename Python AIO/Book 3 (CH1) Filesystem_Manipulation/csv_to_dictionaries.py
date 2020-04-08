import datetime as dt
import csv


# Use these functions to convert any string to appropriate Python data
# type. Get just the first name from full name.
def fname(any):
    try:
        nm = any.split(',')
        return nm[1]
    except IndexError:
        return ''

# Get just the last name from full name.
def lname(any):
    try:
        nm = any.split(',')
        return nm[0]
    except IndexError:
        return ''

# Convert string to integer or zero if no value.
def integer(any):
    return int(any or 0)

# Convert mm/dd/yyyy date to date or None if no valid date.
def date(any):
    try:
        return dt.datetime.strptime(any, "%m/%d/%Y").date()
    except ValueError:
        return None

# Convert any string to Boolean, False if no value.
def boolean(any):
    return bool(any)

# Convert string to float, or to zero if no value.
def floatnum(any):
    s_balance = (any.replace('$', '').replace(',', '')).strip()
    return float(s_balance or 0)

# Create an empty dictionary of people.
people = {}

# Open CSV file with UTF-8 encoding, don't read in newline characters.
with open('sample.csv', encoding='utf-8', newline='') as f:
    # Set up a csv reader with a counter
    reader = enumerate(csv.reader(f))
    # Skip the first row, which is column names.
    f.readline()
    # Loop through remaining rows one at a time, i is counter, row is entire row
    for i, row in reader:
        # From each data row in the CSV file, create a Person object with unique id
        # and appropriate data types, and to people dictionary.
        newdict = dict({'first_name': fname(row[0]), 'last_name': lname(row[0]), 
            'birth_year': integer(row[1]), 'date_joined': date(row[2]), 
            'is_active': boolean(row[3]), 'balance': floatnum(row[4])})
        people[i + 1] = newdict

# When above loop is done, show all objects in the people list.
for person in people.keys():
    id = person
    print(id, people[person]['first_name'], people[person]['last_name'], 
        people[person]['birth_year'], people[person]['date_joined'],
        people[person]['is_active'], people[person]['balance'])
