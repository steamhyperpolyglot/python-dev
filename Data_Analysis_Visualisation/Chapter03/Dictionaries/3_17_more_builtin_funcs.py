Staff_Salary = {
    'Omar Ahmed': 30000,
    'Ali Ziad': 24000,
    'Ossama Hashim': 25000,
    'Majid Hatem': 10000
}

STDMarks = {
    "Salwa Ahmed": 50,
    "Abdullah Mohamed": 80,
    "Sultan Ghanim": 90
}

print(Staff_Salary.get('Ali Ziad'))
print(STDMarks.items())
print(Staff_Salary.keys())

print()
STDMarks.setdefault('Ali Ziad')
print(STDMarks)
print(STDMarks.update(dict1))
print(STDMarks)

dict_items([
    ('Salwa Ahmed', 50),
    ('Abdullah Mohamed', 80),
    ('Sultan Ghanim', 90)
])
dict_keys([
    'Omar Ahmed', 'Ali Ziad', 'Ossama Hashim', 'Majid Hatem'
])