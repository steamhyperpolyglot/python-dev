# not a real solution
def firstlast(sequence):
	return sequence[:1] + sequence[-1:]

t1 = ('a', 'b', 'c')
output1 = firstlast(t1)
print(output1)

t2 = (1, 2, 3, 4)
output2 = firstlast(t2)
print(output2)

print (firstlast('abcd'))