class Point:
    big_prime_1 = 1200556037
    big_prime_2 = 2444555677

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        s = str(self.x) + ', '
        s += str(self.y)
        return s
    
    def __repr__(self):
        s = 'Point(' + str(self.x) + ', '
        s += str(self.y) + ')'
        return s
    
    def __hash__(self):
        n = self.x * big_prime_1
        return (n + self.y) % big_prime_2
    
    def __bool__(self):
        return x and y

pt = Point(3, 4)
print(pt)