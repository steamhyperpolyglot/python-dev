import json
import datetime as dt

# This is the Excel data (no keys)
filename = 'people_from_excel.json'
# Open the file (standard file open stuff
with open(filename, 'r', encoding='utf-8', newline='') as f:
    # Load the whole json file into an object named people
    people = json.load(f)

print(people)
print(type(people))

for p in people:
    # print(type(p))
    name = p['Full Name']
    byear = p['Birth Year']
    # Excel date pretty tricky, use xlrd module
    # y, m, d, h, i, s = xlrd.xldate_as_tuple(p['Date Joined'], 0)
    joined = dt.datetime.strptime(p['Date Joined'], "%m/%d/%Y").date()
    balance = '$' + f"{p['Balance']:,.2f}"
    print(f"{name:<22} {byear} {joined:%m/%d/%Y} {balance:>12}")
