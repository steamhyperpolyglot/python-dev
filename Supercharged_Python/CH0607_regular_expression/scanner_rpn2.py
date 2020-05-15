import re
import operator

the_stk = []

def bin_op(oper):
    op2, op1 = the_stk.pop(), the_stk.pop()
    the_stk.append(oper(op1, op2))

scanner = re.Scanner([
    (r'[+]', lambda s, t: bin_op(operator.add)),
    (r'[*]', lambda s, t: bin_op(operator.mul)),
    (r'[-]', lambda s, t: bin_op(operator.sub)),
    (r'[/]', lambda s, t: bin_op(operator.truediv)),
    (r'\d+\.\d*', lambda s, t: the_stk.append(float(t))),
    (r'\d+', lambda s, t: the_stk.append(int(t))),
    (r'\s+', None)
])

def main():
    input_str = input('Enter RPN string: ')
    tokens, unknown = scanner.scan(input_str)
    if unknown:
        print('Unrecognized input:', unknown)
    else:
        print('Answer is', the_stk.pop())

main()