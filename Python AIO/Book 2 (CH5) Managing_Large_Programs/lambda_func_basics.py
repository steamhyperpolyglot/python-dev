def lowercaseof(anystring):
	""" Converts string to all lowercase """
	return anystring.lower()


names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
# names.sort(key=lowercaseof)
# print(names)

# Now we use the lambda expression/statement
names.sort(key=lambda s: s.lower())
print(names)

# Show number in currency format.
currency = lambda n : f"${n:,.2f}"
# Show number in percent format.
percent = lambda n: f"{n:.2%}"

# Test currency function
print(currency(99))
print(currency(123456789.09876543))

# Test percent function
print(percent(0.065))
print(percent(.5))
