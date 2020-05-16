class Odd:

    def __init__(self):
        self.x = 10
        self.y = 20
        self.__z = 30
    
    def pr(self):
        print('__z = ', self.__z)

o = Odd()
print('x: ', o.x, ', y: ', o.y)