print('Do this first')
try:
    open('people.csv')
except FileNotFoundError:
    print('Cannot find file named people.csv')
except Exception as e:
    print('e')
else:
    print('Show this if no exception.')
finally:
    print('This is the finally block')
print("This is outside the try...except...else...finally")
