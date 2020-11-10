import sys

mylist = []

for i in range(25):
	l = len(mylist)
	s = sys.getsizeof(mylist)
	print(f'len = {l}, size = {s}')
	mylist.append(i)