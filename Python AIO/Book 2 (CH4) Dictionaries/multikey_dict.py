print("Playing with multi-key dictionaries...")

employee = {
	'name': 'Haru Tanaka',
	'year_hired': 2005,
	'dob': '11/23/1987',
	'has_laptop': False
}

print(employee)

product = {
	'name': 'Ray-Ban Wayfarer Sunglasses',
	'unit_price': 112.99,
	'taxable': True,
	'in_stock': 10,
	'models': ['Black', 'Tortise']
}

print('Name:     ', product['name'])
print('Price:    ', f"${product['unit_price']:.2f}")
print('Taxable:  ', product['taxable'])
print('In-stock: ', product['in_stock'])
print('Models:')
for model in product['models']:
	print(" " * 10 + model)