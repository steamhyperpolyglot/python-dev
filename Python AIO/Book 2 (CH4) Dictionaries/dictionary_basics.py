people = {
	'htanaka': 'Haru Tanaka',
	'ppatel': 'Priya Patel',
	'bagarcia': 'Benjamin Alberto Garcia',
	'zmin': 'Zhang Min',
	'afarooqi': 'Ayesha Farooqi',
	'hajackson': 'Hanna Jackson',
	'papatel': 'Pratyush Aarav Patel',
	'hrjackson': 'Henry Jackson'
}

print(people)

print(f"Accessing value for 'zmin': {people['zmin']}")
print(f"Number of items: {len(people)}")
print(f"Does 'hajackson' exists? {'hajackson' in people}")
print(f"Does 'schmeedledorp' exists? {'schmeedledorp' in people}")

# Looking for a person
print("Looking for 'bagarcia'...")
print(people.get('bagarcia'))

# Changing value of an item
people['hajackson'] = "Hanna Jackson-Smith"

# Print the hajackson key to verify that the value has changed.
print(people['hajackson'])

# Change the value of the hrjackson key.
people.update({'hrjackson': 'Henrietta Jackson'})
print(people)

# Update the dictionary with a new property:value pair
people.update({'wwiggins': 'Wanda Wiggins'})
print("\nAdded new key and value:")
print(people)

# Show what's in the data dictionary now.
# for person in people.keys():
# 	print(f"{person:<10}={people[person]:>25}")

# Alternatively, we can use the key,value loop
for key, value in people.items():
	print(f"{key:<10}={value:>25}")

# Next, we can also del items from the data dictionary
# del people["zmin"]

# print("Updated Dictionary:\n")
# print(people)

# Popping and item from the dictionary
zmin = people.pop("zmin")

# Print the dictionary
print(f"{zmin} has been removed from people")
print(people)
