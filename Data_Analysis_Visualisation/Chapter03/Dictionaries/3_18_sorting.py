# Sorting a dictionary
Staff_Salary = {
    'Omar Ahmed': 30000,
    'Ali Ziad': 24000,
    'Ossama Hashim': 25000,
    'Majid Hatem': 10000
}
print("\nSorted by key")
for k in sorted(Staff_Salary):
    print(k, Staff_Salary[k])

print("\nSorted by value")
for w in sorted(Staff_Salary, key=Staff_Salary.get, reverse=True):
    print(w, Staff_Salary[w])