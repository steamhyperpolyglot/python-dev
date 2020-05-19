import numpy as np
import time
import numpy.random as ran


def get_std1(ls):
    t1 = time.time()
    m = sum(ls) / len(ls)
    ls2 = [(i - m) ** 2 for i in ls]
    sd = (sum(ls2) / len(ls2) ** .5)
    t2 = time.time()
    print('Python took', t2 - t1)

def get_std2(A):
    t1 = time.time()
    A2 = (A - np.mean(A)) ** 2
    result = (np.mean(A2)) ** .5
    t2 = time.time()
    print('Numpy took', t2 - t1)

def get_std3(A):
    t1 = time.time()
    result = np.std(A)
    t2 = time.time()
    print('np.std took', t2 - t1)


A = ran.rand(1000000)
get_std1(A)
get_std2(A)
get_std3(A)
