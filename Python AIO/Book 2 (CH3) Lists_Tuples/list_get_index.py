grades = ["C", "B", "A", "D", "C", "B", "C"]

look_for = "F"

# See if the item is in the list
if look_for in grades:
	# If it's in the list, get and show the index.
	print(str(look_for) + " is at index " + str(grades.index(look_for)))
else:
	# If not in the list, don't even try for index number.
	print(str(look_for) + " isn't in the list.")
