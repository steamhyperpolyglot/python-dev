import time

def make_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        print('Time elapsed was', t2 - t1)
        return ret_val
    return wrapper

@make_timer
def count_nums(n):
    for i in range(n):
        for j in range(1000):
            pass

# count_nums = make_timer(count_nums)

count_nums(33000)