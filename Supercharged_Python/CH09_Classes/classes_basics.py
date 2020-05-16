class Pretty:

    def __init__(self, prefix):
        self.prefix = prefix
    
    def print_me(self, a, b, c):
        print(self.prefix, a, sep='')
        print(self.prefix, b, sep='')
        print(self.prefix, c, sep='')


printer = Pretty('-->')
printer.print_me(10, 20, 30)