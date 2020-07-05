Staff_Salary = {
    'Omar Ahmed': 30000,
    'Ali Ziad': 24000,
    'Ossama Hashim': 25000,
    'Majid Hatem': 10000
}
print('Salary package for Ossama Hashim is ', end='')

# access specific dictionary element
print(Staff_Salary['Ossama Hashim'])

# Define a function to return salary after discount tax 5%
def Netsalary(salary):
    return salary - (salary * .05)      # also, could be return salary * .95

# Iterate all elements in a dictionary
print("Name", '\t\t', "Net Salary")
for key, value in Staff_Salary.items():
    print(key, '\t', Netsalary(value))