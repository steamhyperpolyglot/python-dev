import random
print("Numbers that aren't evenly divisible by 5")
counter = 0
while counter < 10:
	# Get a random number
	number = random.randint(1, 999)
	if int(number / 5) == number / 5:
		# If it's even divisible by 5, bail out.
		break
	# Otherwise, print it and keep going for a while.
	print(number)
	# Increment the loop counter
	counter += 1
print("Loop is done")
