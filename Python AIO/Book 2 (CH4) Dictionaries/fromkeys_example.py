# Create a dictionary for products name product.
product = {
	'name': '',
	'unit_price': 0,
	'taxable': True,
	'in_stock': 0,
	'models': []
}

# Create a dictionary named DWC001 that has the same keys as product.
DWC001 = dict.fromkeys(product.keys())
DWC001.setdefault('taxable', True)
DWC001.setdefault('models', [])
DWC001.setdefault('reorder_point', 100)

# Show what's in the new dictionary
print('After using setdefault()...')
print(DWC001)
