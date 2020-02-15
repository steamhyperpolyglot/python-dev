import csv
import datetime as dt

# Open CSV file with UTF-8 encoding, don't read in newline characters
with open('sample.csv', encoding='utf-8', newline='') as f:
    # Create a CSV row counter and row reader.
    reader = enumerate(csv.reader(f))
    # Loop through one row at a time, i is counter, row is entire row.
    for i, row in reader:
        # Row 0 is just column headings, ignore it.
        if i > 0:
            # Whole name split into two at comma.
            try:
                full_name = row[0].split(',')
                # print(full_name)
                # Last name, strip extra spaces.
                last_name = full_name[0].split(' ')[0].strip()
                # First name, strip extra spaces.
                first_name = full_name[0].split(' ')[1].strip()
                birth_year = int(row[1] or 0)
                # Date_joined is a date.
                try:
                    date_joined = dt.datetime.strptime(row[2], "%m/%d/%Y").date()
                except ValueError:
                    date_joined = None
                
                is_active = bool(row[3])
                # Remove $, commas, leading trailing spaces
                str_balance = (row[4].replace('$', '').replace(',', '')).strip()
                balance = float(str_balance or 0)
            except IndexError:
                full_name = last_name = first_name = ""
            print(first_name, last_name, birth_year, date_joined, is_active, balance)

print('Done')
