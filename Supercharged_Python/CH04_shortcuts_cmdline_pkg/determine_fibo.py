def make_fibo_gen(n):
    a, b = 1, 1
    while a <= n:
        yield a, b
        a, b = a + b, a + b

n = int(input('Enter number: '))
if n in make_fibo_gen(n):
    print('number is a Fibonacci.')
else:
    print('number is not a Fibonacci.')