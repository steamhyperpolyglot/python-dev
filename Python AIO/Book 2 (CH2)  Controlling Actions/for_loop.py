for x in range(1, 10):
	print(x)
print("All done")

print("Let's loop through a string...")

my_word = "snorkel"
for x in my_word:
	print(x)
print("Done")

print("Looping through a list...")

for x in ["The", "rain", "in", "Spain"]:
	print(x)
print("Done")

print("Demonstrating how to exit a loop using break...")

# Now how about exiting a loop
answers = ["A", "B", "", "D"]
for answer in answers:
	if answer == "":
		print("Incomplete")
		# break
		continue
		
	print(answer)
print("Loop is done")

# Let's have a nested loop

print("Time for some nested loops")

for outer in ["First", "Second", "Third"]:
	print(outer)
	# Inner loop
	for inner in range(3):
		print(inner + 1)

print("Both loops are done.")
