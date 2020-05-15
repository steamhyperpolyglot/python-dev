import re
pattern = r'\d\d\d-\d\d\d-\d\d\d\d'

s = input('Enter tel. number: ')
if re.match(pattern, s):
    print('Number accepted.')
else:
    print('Incorrect format.')