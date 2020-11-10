from operator import itemgetter

people = [
	{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
	{'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
	{'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}
]

# def person_dict_to_list(d):
# 	return [d['last'], d['first']]

# print(sorted(PEOPLE, key=person_dict_to_list))

# We can also use lambda
# for p in sorted(people,
#                 key=lambda x: [x['last'], x['first']]):
# 	print(f'{p["last"]}, {p["first"]}: {p["email"]}')

# Using itemgetter
for p in sorted(people,
                key=itemgetter('last', 'first')):
	print(f'{p["last"]}, {p["first"]}: {p["email"]}')

# mylist = ['abcd', 'efg', 'hi', 'j']
# mylist = sorted(mylist, key=len)
#
# print(mylist)

# Using itemgetter
# s = 'abcdef'
# t = (10, 20, 30, 40, 50, 60)
# get_2_and_4 = itemgetter(2, 4)
# print(get_2_and_4(s))
# print(get_2_and_4(t))