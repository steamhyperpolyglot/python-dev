prices = (29.95, 9.98, 4.95, 79.98, 2.95)

print(len(prices))

# Loop through and display each item in the tuple.
for price in prices:
	print(f"${price:.2f}")
