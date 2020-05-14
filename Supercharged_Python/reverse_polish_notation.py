the_stack = []

def push(v):
    the_stack.append(v)

def pop():
    return the_stack.pop()

def main():
    s = input('Enter RPN string: ')
    a_list = s.split()
    for item in a_list:
        if item in '+-*/':
            op2 = pop()
            op1 = pop()
            if item == '+':
                push(op1 + op2)
            elif item == '-':
                push(op1 - op2)
            elif item == '*':
                push(op1 * op2)
            else:
                push(op1 / op2)
        else:
            push(float(item))
    print(pop())

main()