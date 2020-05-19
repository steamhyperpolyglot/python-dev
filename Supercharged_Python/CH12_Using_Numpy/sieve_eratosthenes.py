import numpy as np
import time

def sieve(n):
    b_list = [True] * (n + 1)
    for i in range(2, n + 1):
        if b_list[i]:
            for j in range(i * i, n + 1, i):
                b_list[j] = False
    primes = [i for i in range(2, n + 1) if b_list[i]]
    return primes

def np_sieve(n):
    t1 = time.time() * 1000
    # Create B, setting all elements to True.
    B = np.ones(n + 1, dtype=np.bool)
    B[0:2] = False
    for i in range(2, n + 1):
        if B[i]:
            B[i * i: n + 1: i] = False
    t2 = time.time() * 1000
    print('np_sieve took', t2 - t1, 'milliseconds.')
    return np.arange(n + 1)[B]


np_sieve(10000)