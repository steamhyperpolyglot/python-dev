import random
print("Odd numbers")
counter = 0
while counter < 10:
	# Get a random number
	number = random.randint(1,999)
	if int(number / 2) == number / 2:
		# If it's an even number, don't print it
		continue
	# Otherwise, if it's odd, print it and increment the counter
	print(number)
	# Increment the loop counter.
	counter += 1
print("Loop is done")
