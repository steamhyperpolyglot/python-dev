def avg(a_list):
    '''This function finds the average val in a list.'''
    x = (sum(a_list) / len(a_list))
    print('The average is:', x)
    return x

def new_func(a_list):
    return (sum(a_list) / len(a_list))

def func_info(func):
    print('Function name:', func.__name__)
    print('Function documentation:')
    help(func)

old_avg = avg
avg = new_func

print(func_info(old_avg))