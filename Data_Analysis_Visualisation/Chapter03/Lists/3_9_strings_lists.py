# convert string to a list of characters
Word = 'Egypt'
List1 = list(Word)
print(List1)

# use the delimiter
Greeting = 'Welcome-to-Egypt'
List2 = Greeting.split("-")
print(List2)

Greeting = 'Welcome-to-Egypt'
delimiter = '-'
List2 = Greeting.split(delimiter)
print(List2)

# we can break a string into words using the split method
Greeting = 'Welcome to Egypt'
List2 = Greeting.split()