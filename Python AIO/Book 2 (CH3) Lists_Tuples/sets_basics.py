sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}

sample_set.add(11.23)

# Adding items to the set
sample_set.update([88, 123.45, 2.98])

print(f"Updated set: {sample_set}")

# Make a copy and show the copy
ss2 = sample_set.copy()
print(ss2)

# Loop through the set and print each item right-aligned and formatted
print("\nLoop through set and print each item formatted.")
for price in sample_set:
	print(f"{price:>6.2f}")

