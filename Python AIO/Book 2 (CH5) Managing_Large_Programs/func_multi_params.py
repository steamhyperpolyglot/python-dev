def hello(fname, lname, datestring=''):
	""" A docstring describing the function """
	msg = 'Hello ' + fname + ' ' + lname
	if len(datestring) > 0:
		msg += ' you mentioned ' + datestring
	print(msg)


hello('Sherman', 'Chen', '12/31/2019')
hello('Alan', 'Tan')
