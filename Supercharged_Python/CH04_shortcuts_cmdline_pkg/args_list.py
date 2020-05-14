def my_var_func(*args):
    print('The number of args is', len(args))
    for item in args:
        print(item)

my_var_func(10, 20, 30, 40)

def avg(*args):
    return sum(args) / len(args)

def avg(units, *args):
    print(sum(args) / len(args), units)

# print(avg(11, 22, 33))
# print(avg(1, 2))
print(avg('inches', 11, 22, 33))