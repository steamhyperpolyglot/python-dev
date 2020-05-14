import sys

def quad(a, b, c):
    '''Quadratic Formula function.'''

    determin = (b * b - 4 * a * c) ** .5
    x1 = (-b + determin) / (2 * a)
    x2 = (-b - determin) / (2 * a)
    return x1, x2

def main():
    '''Get argument values, convert, call quad.'''
    # s1, s2, s3 = sys.argv[1], sys.argv[2], sys.argv[3]
    if len(sys.argv) > 3:
        s1, s2, s3 = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        s1 = input('Enter a: ')
        s2 = input('Enter b: ')
        s3 = input('Enter c: ')
    
    a, b, c = float(s1), float(s2), float(s3)
    x1, x2 = quad(a, b, c)
    print('x values: {}, {}.'.format(x1, x2))

main()