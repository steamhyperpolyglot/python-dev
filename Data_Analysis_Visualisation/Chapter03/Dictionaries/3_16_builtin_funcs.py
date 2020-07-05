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

def cmp(a, b):
    for key, value in a.items():
        for key1, value1 in b.items():
            return (key > key1) - (key < key1)

print(cmp(STDMarks, Staff_Salary))
print(cmp(STDMarks, STDMarks))
print(len(STDMarks))
print(str(STDMarks))
print(type(STDMarks))