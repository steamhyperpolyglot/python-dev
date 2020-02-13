# Create a generic dictionary to contain multiple product dictionaries
products = {
	'RB00111': {'name': 'Rayban Sunglasses', 'price': 112.98, 'models': ['black', 'tortoise']},
	'DWC0317': {'name': 'Drone with Camera', 'price': 73.95, 'models': ['white', 'black']},
	'MTS0540': {'name': 'T-Shirt', 'price': 2.95, 'models': ['small', 'medium', 'large']},
	'ECD2989': {'name': 'Echo Dot', 'price': 29.99, 'models': []}
}

print(f"{'ID':<6} {' Name':<17} {'Price':>8} {'  Models':<22}")
print('-' * 60)

# Loop through each dictionary in the products dictionary
for oneproduct in products.keys():
	# Get the id of one product.
	id = oneproduct
	# Get the name of one product.
	name = products[oneproduct]['name']
	# Get the unit price of one product and format with $
	unit_price = '$' + f"{products[oneproduct]['price']:,.2f}"
	# Create an empty string variable named models
	models = ''
	# Loop through the models list and tack ont models
	# one item from the list followed by a comma and a space.
	for m in products[oneproduct]['models']:
		models += m + ', '
	# If the models variable is more than two characters in length,
	# Peel off the last two characters (last comma and space)
	if len(models) > 2:
		models = models[:-2]
	else:
		models = "<none>"
	
	# Print all the variables with a neat f-string.
	print(f"{id:<6} {name:<17} {unit_price:>8}  {models:<22}")
