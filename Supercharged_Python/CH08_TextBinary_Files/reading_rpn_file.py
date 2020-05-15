import re
import operator

sym_tab= {}
stack = []      # Stack to hold the values.

# Scanner object. Isolate each token and take
# appropriate action: push a numeric value, 
# but perform operation on top two elements on
# stack if an operator is found.

scanner = re.Scanner([
    (r"[ \t\n]", lambda s, t: None),
    (r"-?(\d*\.)?\d+", lambda s, t: stack.append(float(t))),
    (r"[a-zA-Z_][a-zA-Z_0-9]*", lambda s, t: stack.append(t)),
    (r"\d+", lambda s, t: stack.append(int(t))),
    (r"[+]", lambda s, t: bin_op(operator.add)),
    (r"[-]", lambda s, t: bin_op(operator.sub)),
    (r"[*]", lambda s, t: bin_op(operator.mul)),
    (r"[/]", lambda s, t: bin_op(operator.truediv)),
    (r"[\^]", lambda s, t: bin_op(operator.pow)),
    (r"[=]", lambda s, t: assign_op()),
])

# Binary Operator function. pop top two elements
# from stack and push the result back on the stack.

def bin_op(action):
    '''
    Binary Operation evaluator: If an operand is
    a variable name, look it up in the symbol table
    and replace with the corresponding value, before
    being evaluated.
    '''
    op2, op1 = stack.pop(), stack.pop()
    if type(op1) == str:
        op1 = sym_tab[op1]
    if type(op2) == str:
        op2 = sym_tab[op2]
    stack.append(action(op1, op2))

def assign_op():
    '''
    Assignment Operator function: Pop off a name
    and a value, and make a symbol-table entry.
    Remember to look up op2 in the symbol table
    if  it is a string.
    '''
    op2, op1 = stack.pop(), stack.pop()
    if type(op2) == str:    # Source may be another var!
        op2 = sym_tab[op2]
    sym_tab[op1] = op2

def open_rpn_file():
    '''
    Open-source file function. Open a named file and read
    lines into a list, which is returned.
    '''
    while True:
        try:
            fname = input('Enter RPN source: ')
            f = open(fname, 'r')
            if not f:
                return None
            else:
                break
        
        except:
            print('File not found. Re-enter.')
        
        a_list = f.readlines()
        return a_list

def open_rpn_file():
    '''
    Open source file function. Open a named
    file and read lines into a list, which is
    returned.
    '''
    while True:
        try:
            fname = input('Enter RPN source: ')
            f = open(fname, 'r')
            if not f:
                return None
            else:
                break
        except:
            print('File not found. Re-enter.')
    a_list = f.readlines()
    return a_list

def main():
    a_list = open_rpn_file()
    if not a_list:
        print('Bye!')
        return 

    for a_line in a_list:
        a_line = a_line.strip()
        if a_line:
            tokens, unknown = scanner.scan(a_line)
            if unknown:
                print('Unrecognized input:', unknown)
    print(str(stack[-1]))

main()