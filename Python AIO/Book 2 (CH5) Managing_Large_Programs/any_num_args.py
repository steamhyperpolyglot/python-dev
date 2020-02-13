def sorter(*args):
	"""
	Pass in any number of arguments separated by commas
	Inside the function, they are treated as a tuple named args
	"""
	newlist = list(args)
	# Sort and show the list.
	newlist.sort()
	print(newlist)


sorter(1, 0.001, 1, 2, 10000)
